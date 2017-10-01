from .adscommand import AdsCommand
from .deviceinforesponse import DeviceInfoResponse

class DeviceInfoCommand(AdsCommand):

    def __init__(self):
        self.CommandID = 0x0001


    def CreateRequest(self):
        return b''


    def CreateResponse(self, responsePacket):
        return DeviceInfoResponse(responsePacket)