import struct
from .. import AmsPacket
from adsresponse import AdsResponse

class ReadResponse(AdsResponse):
    
    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)
        
        self.Length = struct.unpack_from('I', responseAmsPacket.Data, 4)[0]
        self.Data = responseAmsPacket.Data[8:]
        
        
    Length = 0
    
    Data = '0'
    
    
    def __str__(self):
        result = "AdsReadResponse:\n"
        result += AmsPacket.GetHexStringBlock(self.Data)
        return result
                
