import time
import select
import socket
import struct
import threading
from amspacket import AmsPacket
from commands import *

class AdsClient:
    
    def __init__(self, adsConnection):
        self.AdsConnection = adsConnection
        pass
    
    
    AdsConnection = None
    
    
    AdsPortDefault = 0xBF02
    
    
    Socket = None
    
    
    def Close(self):
        if (self.Socket != None):
            self.Socket.close()
            self.Socket = None
    
    
    
    def Connect(self):
        self.Close()
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Socket.settimeout(3)
        self.Socket.connect((self.AdsConnection.TargetIP, self.AdsPortDefault))        
        
    
    
    """
    def _BeginAsyncRead(self):
        self.Socket.settimeout(0)
        self.Socket.setblocking(0)
        
        self._AsyncReadThread = threading.Thread(target=self.Foo)
        self._AsyncReadThread.start()
        
        
    def AsyncReadAproach(self):
        
        while (True):
            ready = select.select([self.Socket], [], [], 1)
            if ready[0]:
                newAmsPackt = self.ReadAmsPacketFromSocket()
                ...?
                ...?
                ...?            
    """    
        
    
    def ReadAmsPacketFromSocket(self):
        chunkSize = 1024
        
        response = self.Socket.recv(chunkSize)
        
        # ensure correct beckhoff tcp header
        if(len(response) < 6):
            return None
        
        # first two bits must be 0
        if (response[0:2] != '\x00\x00'):
            return None
        
        # read whole data length
        dataLen = struct.unpack('I', response[2:6])[0] + 6
        
        # read rest of data, if any
        while (True):
            chunk = max(0, min(chunkSize, dataLen - len(response)))
            if(chunk > 0):
                response += self.Socket.recv(chunk)
            else:             
                break

        # cut off tcp-header and return response amspacket
        return AmsPacket.FromBinaryData(response[6:])
        
        
    def GetTcpHeader(self, amsData):
        # pack 2 bytes (reserved) and 4 bytes (length)
        # format _must_ be little endian!
        return struct.pack('<HI', 0, len(amsData))  
    
    
    def SendAndRecv(self, amspacket):        
        if (self.Socket == None):
            self.Connect()
        
        # get ams-data and generate tcp-header
        amsData = amspacket.GetBinaryData()
        tcpHeader = self.GetTcpHeader(amsData)
        
        self.zipfi = None
        
        # send tcp-header and ams-data
        self.Socket.send(tcpHeader + amsData)
        
        result = self.ReadAmsPacketFromSocket()
        return result

    

    def ReadDeviceInfo(self):
        return DeviceInfoCommand().Execute(self)


    def Read(self, indexGroup, indexOffset, length):
        return ReadCommand(indexGroup, indexOffset, length).Execute(self)

    
    def Write(self, indexGroup, indexOffset, data):
        return WriteCommand(indexGroup, indexOffset, data).Execute(self)

    
    def ReadState(self):
        return ReadStateCommand().Execute(self)
    
    
    def WriteControl(self, adsState, deviceState, data = ''):
        return WriteControlCommand(adsState, deviceState, data).Execute(self)


    def AddDeviceNotification(self):
        raise NotImplementedError()
    
    
    def DeleteDeviceNotification(self):
        raise NotImplementedError()


    def ReadWrite(self, indexGroup, indexOffset, readLen, dataToWrite = ''):
        return ReadWriteCommand(indexGroup, indexOffset, readLen, dataToWrite).Execute(self)
        
    """
    def TEST(self):
        packet = AmsPacket(self.AdsConnection)
        packet.CommandID = 0x0001
        packet.StateFlags = 0x0004
        
        print("%s" % packet)
        
        foobar = self.SendAndRecv(packet)
        
        print("%s" % foobar)
    """