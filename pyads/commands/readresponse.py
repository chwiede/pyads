import ctypes
import struct
from adsresponse import AdsResponse
from .. import adstools


class ReadResponse(AdsResponse):
    
    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)
        
        self.Length = struct.unpack_from('I', responseAmsPacket.Data, 4)[0]
        self.Data = responseAmsPacket.Data[8:]
        
        
    Length = 0
    
    Data = '0'
    
    
    def __str__(self):
        result = "AdsReadResponse:\n"
        result += adstools.HexBlock(self.Data)
        return result
    
    
    def CreateBuffer(self):
        return ctypes.create_string_buffer(self.Data, len(self.Data))                
                
