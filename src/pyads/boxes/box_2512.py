from box import Box, BoxType

from .. import AdsDatatype
from .. import AdsClient
from .. import SymbolInfo

class Box2512(Box):
    
    def __init__(self, descriptor):
        Box.__init__(self, descriptor)
        self.SizeIn = 8
        self.SizeOut = 8
        self.BoxType = BoxType.Complex | BoxType.Input | BoxType.Output


    def __str__(self):
        return "KL2512 PWM-Output (2 Channels)"

    def CreateSymbolInfos(self):
        result = []
        
        for i in range(2):
            offset = self.OffsetIn + i*4 + 2 
            result.append(SymbolInfo("Chn%s" % i, AdsClient.AdsIndexGroupOut, offset, AdsDatatype.UInt16))
        
        return result
