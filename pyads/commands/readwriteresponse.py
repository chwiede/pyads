import struct
from .. import AmsPacket
from .adsresponse import AdsResponse

class ReadWriteResponse(AdsResponse):

    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)

        self.Length = struct.unpack_from('I', responseAmsPacket.Data, 4)[0]
        self.Data = responseAmsPacket.Data[8:]


    Length = 0

    Data = b'0'


    def __str__(self):
        result = "AdsReadWriteResponse:\n"
        result += AmsPacket.GetHexStringBlock(self.Data)
        return result
