import struct
from adsclient import AdsClient
from adsdatatype import AdsDatatype
from adsconnection import AdsConnection
from binaryparser import BinaryParser
from boxes import Box

class AdsDevice(AdsClient):

    def __init__(self, adsConnection):
        AdsClient.__init__(self, adsConnection)


    def GetSymbolHandle(self, variableName):
        symbolData = self.ReadWrite(0xF003, 0x0000, 4, variableName + '\x00').Data
        symbolHandle = struct.unpack("I", symbolData)[0]
        return symbolHandle        


    def ReadByName(self, variableName, adsDatatype):
        symbolHandle = self.GetSymbolHandle(variableName)
        return self.ReadByHandle(symbolHandle, adsDatatype)
        

    def ReadByHandle(self, symbolHandle, adsDatatype):
        length = AdsDatatype.GetSize(adsDatatype)
        data = self.Read(0xF005, symbolHandle, length).Data
        return AdsDatatype.Unpack(data, adsDatatype)


    def WriteByName(self, variableName, adsDatatype, value):
        symbolHandle = self.GetSymbolHandle(variableName)
        self.WriteByHandle(symbolHandle, adsDatatype, value)


    def WriteByHandle(self, symbolHandle, adsDatatype, value):
        valueRaw = AdsDatatype.Pack(value, adsDatatype)
        self.Write(0xF005, symbolHandle, valueRaw)


    def ScanBoxes(self):
        connection = AdsConnection()
        connection.TargetIP = self.AdsConnection.TargetIP
        
        connection.TargetAmsID = self.AdsConnection.TargetAmsID
        connection.TargetAmsPort = 100
        
        connection.SourceAmsID = self.AdsConnection.SourceAmsID
        connection.SourceAmsPort = self.AdsConnection.SourceAmsPort
        
        tmpClient = AdsClient(connection)
        
        try:
            result = []
            data = tmpClient.Read(0x00000000, 0x00090000, 512).Data
            binary = BinaryParser(data)
            for i in range(64):
                boxID = binary.ReadUInt16()
                if(boxID > 0):
                    result.append(Box(boxID))
            
            return result                
            
        finally:            
            tmpClient.Close()
            
                