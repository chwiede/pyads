import struct

class AdsResponse:

    def __init__(self, responseAmsPacket):
        self.Error = struct.unpack_from('I', responseAmsPacket.Data)[0]
        

    Error = 0