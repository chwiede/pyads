import struct
from .. import AdsException

class AdsResponse:

    def __init__(self, responseAmsPacket):
        self.Error = struct.unpack_from('I', responseAmsPacket.Data)[0]

        if (self.Error > 0):
            raise AdsException(self.Error)


    Error = 0