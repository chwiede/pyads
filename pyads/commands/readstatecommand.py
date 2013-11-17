from adscommand import AdsCommand
from readstateresponse import ReadStateResponse

class ReadStateCommand(AdsCommand):
    
    def __init__(self):
        self.CommandID = 0x0004
        
        
    def CreateRequest(self):
        return ''
    
    
    def CreateResponse(self, responsePacket):
        return ReadStateResponse(responsePacket)