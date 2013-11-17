import copy
import struct
from .adsclient import AdsClient
from .adsdatatype import AdsDatatype
from .adsconnection import AdsConnection
from .binaryparser import BinaryParser

class AdsDevice(AdsClient):

    def __init__(self, adsConnection = None, amsTarget = None, amsSource = None):
        AdsClient.__init__(self, adsConnection, amsTarget, amsSource)
        
        
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
