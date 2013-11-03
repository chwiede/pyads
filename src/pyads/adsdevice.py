import copy
import struct
import boxes
from adsclient import AdsClient
from adsdatatype import AdsDatatype
from adsconnection import AdsConnection
from binaryparser import BinaryParser
from boxes.box import Box

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
        
        
    def GetBoxDescriptors(self):
        connection = copy.deepcopy(self.AdsConnection)
        connection.TargetAmsPort = 100
        
        tmpClient = AdsClient(connection)
        
        try:
            data = tmpClient.Read(0x00000000, 0x00090000, 512).Data
            descriptors = struct.unpack('H' * 256, data)
            return filter(lambda x: x != 0, descriptors)
        finally:
            tmpClient.Close()
            

    def GetBoxes(self):
        totalOffsetIn = 0
        totalOffsetOut = 0
        descriptors = self.GetBoxDescriptors()
        
        result = []
        
        for descriptor in descriptors:
            box = boxes.Create(descriptor)
            box.OffsetIn = totalOffsetIn
            box.OffsetOut = totalOffsetOut
            
            result.append(box)
            
            totalOffsetIn += box.SizeIn
            totalOffsetOut += box.SizeOut
            
        return result
            
                