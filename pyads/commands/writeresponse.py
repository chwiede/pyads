import struct
from .. import AmsPacket
from .adsresponse import AdsResponse

class WriteResponse(AdsResponse):

    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)
