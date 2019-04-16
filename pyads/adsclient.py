import time
import select
import socket
import struct
import threading
import errno

from .amspacket import AmsPacket
from .adsconnection import AdsConnection
from .adsexception import AdsException
from .commands import *

class InvalidPacket(AdsException):
    pass

class AdsClient:

    def __init__(self, adsConnection = None, amsTarget = None, amsSource = None, targetIP = None):
        if adsConnection != None and amsTarget == None and amsSource == None:
            self.AdsConnection = adsConnection

        elif amsTarget != None and adsConnection == None:
            self.AdsConnection = AdsConnection(amsTarget, amsSource, targetIP)

        else:
            raise Exception('You must specify either connection or adsTarget, not both.')

        self.response = b''

    MAX_RETRY_ON_FAIL = 3

    Debug = False

    RetryOnFail = 0

    AdsConnection = None

    AdsPortDefault = 0xBF02

    AdsIndexGroupIn = 0xF020

    AdsIndexGroupOut = 0xF030

    AdsChunkSizeDefault = 1024

    Socket = None

    _CurrentInvokeID = 0x8000

    _CurrentPacket = None

    _CurrentError = None

    @property
    def IsConnected(self):
        return self.Socket != None and self.Socket.fileno() >= 0


    def Close(self):
        if (self.Socket != None):
            self.Socket.close()
            self.Socket = None



    def Connect(self):
        self.Close()
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.settimeout(2)

        try:
            self.Socket.connect((self.AdsConnection.TargetIP, self.AdsPortDefault))
            self._BeginAsyncRead()
        except socket.error:
            raise AdsException(0x274c)



    def _BeginAsyncRead(self):
        self._AsyncReadThread = threading.Thread(target=self._AsyncRead)
        self._AsyncReadThread.start()


    def _AsyncRead(self):

        while self.IsConnected:
            try:
                ready = select.select([self.Socket], [], [], 0.1)

                if ready[0] and self.IsConnected:
                    newPacket = self.ReadAmsPacketFromSocket()
                    if newPacket.InvokeID == self._CurrentInvokeID:
                        self._CurrentPacket = newPacket
                    else:
                        print("Packet dropped:")
                        print(newPacket)
            except (socket.error, select.error, InvalidPacket) as e:
                self.Close()
                self._CurrentError = e
                break



    def ReadAmsPacketFromSocket(self):

        # generate packet from cache, or read more data from recv buffer.
        if len(self.response) == 0:
            response = self.Socket.recv(self.AdsChunkSizeDefault)
        else:
            response = self.response

        # ensure correct beckhoff tcp header
        if(len(response) < 6):
            raise InvalidPacket('Invalid packet received')

        # first two bits must be 0
        if (response[0:2] != b'\x00\x00'):
            raise InvalidPacket('Invalid packet received')

        # read whole data length
        dataLen = struct.unpack('I', response[2:6])[0] + 6

        # read rest of data, if any
        while (len(response) < dataLen):
            nextReadLen = min(self.AdsChunkSizeDefault, dataLen - len(response))
            response += self.Socket.recv(nextReadLen)

        # cut off tcp-header and return response amspacket
        packet = AmsPacket.FromBinaryData(response[6:dataLen])
        self.response = response[dataLen:]
        return packet


    def GetTcpHeader(self, amsData):
        # pack 2 bytes (reserved) and 4 bytes (length)
        # format _must_ be little endian!
        return struct.pack('<HI', 0, len(amsData))


    def SendAndRecv(self, amspacket):

        if not self.IsConnected:
            self.Connect()

        # prepare packet with invoke id
        self.PrepareCommandInvoke(amspacket)

        # send tcp-header and ams-data
        try:
            self.Socket.send(self.GetTCPPacket(amspacket))
        except socket.error as e:
            # if i fail Socket.send i try again for 3 times
            if self.RetryOnFail < self.MAX_RETRY_ON_FAIL:
                self.RetryOnFail += 1
                # if i have a BROKEN PIPE error i reconnect
                # the socket before try again
                if e.errno == errno.EPIPE:
                    self.Connect()
                return self.SendAndRecv(amspacket)
            else:
                self.RetryOnFail = 0
                raise AdsException(0x274c)

        # here's your packet
        return self.AwaitCommandInvoke()



    def GetTCPPacket(self, amspacket):

        # get ams-data and generate tcp-header
        amsData = amspacket.GetBinaryData()
        tcpHeader = self.GetTcpHeader(amsData)

        return tcpHeader + amsData



    def PrepareCommandInvoke(self, amspacket):
        if(self._CurrentInvokeID < 0xFFFF):
            self._CurrentInvokeID += 1
        else:
            self._CurrentInvokeID = 0x8000

        self._CurrentPacket = None
        self._CurrentError = None
        amspacket.InvokeID = self._CurrentInvokeID

        if self.Debug:
            print(">>> sending ams-packet:")
            print(amspacket)



    def AwaitCommandInvoke(self):
        # unfortunately threading.event is slower than this oldschool poll :-(
        timeout = 0
        while (self._CurrentPacket == None):
            if self._CurrentError:
                raise self._CurrentError
            timeout += 0.001
            time.sleep(0.001)
            if (timeout > 10):
                raise AdsException(0x745)

        if self.Debug:
            print("<<< received ams-packet:")
            print(self._CurrentPacket)

        return self._CurrentPacket




    def ReadDeviceInfo(self):
        return DeviceInfoCommand().Execute(self)


    def Read(self, indexGroup, indexOffset, length):
        return ReadCommand(indexGroup, indexOffset, length).Execute(self)


    def Write(self, indexGroup, indexOffset, data):
        return WriteCommand(indexGroup, indexOffset, data).Execute(self)


    def ReadState(self):
        return ReadStateCommand().Execute(self)


    def WriteControl(self, adsState, deviceState, data = b''):
        return WriteControlCommand(adsState, deviceState, data).Execute(self)


    def AddDeviceNotification(self):
        raise NotImplementedError()


    def DeleteDeviceNotification(self):
        raise NotImplementedError()


    def ReadWrite(self, indexGroup, indexOffset, readLen, dataToWrite = b''):
        return ReadWriteCommand(indexGroup, indexOffset, readLen, dataToWrite).Execute(self)


    def __enter__(self):
        return self


    def __exit__(self, vtype, value, traceback):
        self.Close()

