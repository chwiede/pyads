import struct
from .adsresponse import AdsResponse

class ReadStateResponse(AdsResponse):

    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)

        self.AdsState = struct.unpack_from('H', responseAmsPacket.Data, 4)[0]
        self.DeviceState = struct.unpack_from('H', responseAmsPacket.Data, 6)[0]


    AdsState = 0

    DeviceState = 0


    def __str__(self):
        return "Ads/Device State: %s/%s" % (self.AdsState, self.DeviceState)

