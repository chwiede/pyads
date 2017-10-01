from .adscommand import AdsCommand
from .readstateresponse import ReadStateResponse

class ReadStateCommand(AdsCommand):

    def __init__(self):
        self.CommandID = 0x0004


    def CreateRequest(self):
        return b''


    def CreateResponse(self, responsePacket):
        return ReadStateResponse(responsePacket)
