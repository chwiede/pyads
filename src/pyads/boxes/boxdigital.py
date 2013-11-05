from box import Box, BoxType

from .. import AdsDatatype
from .. import AdsClient
from .. import SymbolInfo

class BoxDigital(Box):
    
    def __init__(self, descriptor):
        Box.__init__(self, descriptor)
        self.Channels = BoxType.GetChannelCount(descriptor)
        
        if (self.IsInput):
            self.SizeIn = BoxType.GetBoxBitLength(descriptor)
        
        if (self.IsOutput):
            self.SizeOut = BoxType.GetBoxBitLength(descriptor) 
        
        
    Channels = 0
    
    def CreateSymbolInfos(self):
        result = []
        
        if (self.IsInput):
            for c in range(self.Channels):
                result.append(SymbolInfo(
                    "channel%s" % c,
                    AdsClient.AdsIndexGroupIn,
                    self.OffsetIn,
                    AdsDatatype.Bool,
                    c                    
                ))
        
        if (self.IsOutput):
            for c in range(self.Channels):
                result.append(SymbolInfo(
                    "channel%s" % c,
                    AdsClient.AdsIndexGroupOut,
                    self.OffsetOut,
                    AdsDatatype.Bool,
                    c                    
                ))

        return result
                           
        
    