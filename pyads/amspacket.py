from .binaryparser import BinaryParser
import pyads

class AmsPacket():

    def __init__(self, connection = None):
        if(connection != None):
            self.TargetAmsID = connection.TargetAmsID
            self.TargetAmsPort = connection.TargetAmsPort
            self.SourceAmsID = connection.SourceAmsID
            self.SourceAmsPort = connection.SourceAmsPort



    TargetAmsID = ''
    """the ams-net-id of the destination device (6 bytes)"""

    TargetAmsPort = 0
    """the ams-port to use (2 bytes, UInt16)"""

    SourceAmsID = '0'
    """the ams-net-id of the sender device (6 bytes)"""

    SourceAmsPort = 0
    """the ams-port of the sender (2 bytes, UInt16)"""

    CommandID = 0
    """command-id (2 bytes, UInt16)"""

    StateFlags = 0
    """state flags, i.e. 0x0004 for request. (2 bytes, UInt16)"""

    Length = 0
    """length of data (4 bytes, UInt32)"""

    ErrorCode = 0
    """error code of ads-response (4 bytes, UInt32)"""

    InvokeID = 0
    """free choosable number to identify request<->response  (4 bytes, UInt32)"""

    Data = b''
    """the ads-data to transmit"""


    @staticmethod
    def AmsNetIDToBytes(pointDottedBytes):
        return list(map(int, pointDottedBytes.split('.')))



    @staticmethod
    def AmsNetIDFromBytes(byteList):
        words = []

        for bt in byteList:
            words.append("%s" % ord(bt))

        return ".".join(words)



    def GetBinaryData(self):
        binary = BinaryParser()

        # tcp/ip header
        #binary.WriteUInt16(0)
        #binary.WriteUInt32(32 + len(self.Data))

        # amsheader
        # ams-target id & port
        binary.WriteBytes(AmsPacket.AmsNetIDToBytes(self.TargetAmsID))
        binary.WriteUInt16(self.TargetAmsPort)

        # ams-source id & port
        binary.WriteBytes(AmsPacket.AmsNetIDToBytes(self.SourceAmsID))
        binary.WriteUInt16(self.SourceAmsPort)

        # command id, state flags & data length
        binary.WriteUInt16(self.CommandID)
        binary.WriteUInt16(self.StateFlags)
        binary.WriteUInt32(len(self.Data))

        # error code & invoke id
        binary.WriteUInt32(self.ErrorCode)
        binary.WriteUInt32(self.InvokeID)

        # last but not least - the data
        binary.WriteBytes(self.Data)

        # return byte buffer
        return binary.ByteData


    @staticmethod
    def FromBinaryData(data = ''):
        binary = BinaryParser(data)
        result = AmsPacket()

        # amsheader
        # ams-target id & port
        result.TargetAmsID = AmsPacket.AmsNetIDFromBytes(binary.ReadBytes(6))
        result.TargetAmsPort = binary.ReadUInt16()

        # ams-source id & port
        result.SourceAmsID = AmsPacket.AmsNetIDFromBytes(binary.ReadBytes(6))
        result.SourceAmsPort = binary.ReadUInt16()

        # command id, state flags & data length
        result.CommandID = binary.ReadUInt16()
        result.StateFlags = binary.ReadUInt16()
        result.Length = binary.ReadUInt32()

        # error code & invoke id
        result.ErrorCode = binary.ReadUInt32()
        result.InvokeID = binary.ReadUInt32()

        # last but not least - the data
        result.Data = binary.ByteData[32:]

        # ready, give out!
        return result




    def __str__(self):
        result = "FROM %s:%s --> " % (self.SourceAmsID, self.SourceAmsPort)
        result += "%s:%s\n" % (self.TargetAmsID, self.TargetAmsPort)
        result += "Command ID:  %s\n" % self.CommandID
        result += "Invoke ID:   %s\n" % self.InvokeID
        result += "State Flags: %s\n" % self.StateFlags
        result += "Data Length: %s\n" % self.Length
        result += "Error:       %s\n" % self.ErrorCode

        if (len(self.Data) == 0):
            result += "Packet contains no data.\n"
        else:
            result += "Data:\n%s\n" % pyads.HexBlock(self.Data)

        return result
