import struct
from .adsresponse import AdsResponse

class WriteControlResponse(AdsResponse):

    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)

