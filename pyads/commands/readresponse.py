import ctypes
import struct
import pyads
from .adsresponse import AdsResponse

class ReadResponse(AdsResponse):

    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)

        self.Length = struct.unpack_from('I', responseAmsPacket.Data, 4)[0]
        self.Data = responseAmsPacket.Data[8:]


    Length = 0

    Data = b'0'

    def __str__(self):
        result = "AdsReadResponse:\n"
        result += pyads.HexBlock(self.Data)
        return result


    def CreateBuffer(self):
        return ctypes.create_string_buffer(self.Data, len(self.Data))

