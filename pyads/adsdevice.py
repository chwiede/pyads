import copy
import struct
from .adsclient import AdsClient
from .adsdatatype import AdsDatatype
from .adsconnection import AdsConnection
from .binaryparser import BinaryParser

class AdsDevice(AdsClient):

    def __init__(self, adsConnection = None, amsTarget = None, amsSource = None, targetIP = None):
        AdsClient.__init__(self, adsConnection, amsTarget, amsSource, targetIP)


    def GetSymbolHandle(self, variableName):
        symbolData = self.ReadWrite(0xF003, 0x0000, 4, variableName.encode('ascii') + b'\x00').Data
        symbolHandle = struct.unpack("I", symbolData)[0]
        return symbolHandle


    def ReadByName(self, variableName, adsDatatype, length = None):
        symbolHandle = self.GetSymbolHandle(variableName)
        return self.ReadByHandle(symbolHandle, adsDatatype, length)


    def ReadByHandle(self, symbolHandle, adsDatatype, length = None):
        if length is None:
            length = AdsDatatype.GetSize(adsDatatype)
        data = self.Read(0xF005, symbolHandle, length).Data
        return AdsDatatype.Unpack(data, adsDatatype)


    def WriteByName(self, variableName, adsDatatype, value):
        symbolHandle = self.GetSymbolHandle(variableName)
        self.WriteByHandle(symbolHandle, adsDatatype, value)


    def WriteByHandle(self, symbolHandle, adsDatatype, value):
        valueRaw = AdsDatatype.Pack(value, adsDatatype)
        self.Write(0xF005, symbolHandle, valueRaw)
