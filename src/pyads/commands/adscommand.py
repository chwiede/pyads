from .. import AmsPacket
from .. import AdsException

class AdsCommand:
    
    def __init__(self):
        pass
    
    
    CommandID = 0
    
    
    def CreateRequest(self):
        raise NotImplementedError()
    
    
    def CreateResponse(self, responsePacket):
        raise NotImplementedError()
    
    
    def Execute(self, adsClient):
        
        # create packet
        packet = AmsPacket(adsClient.AdsConnection)
        packet.CommandID = self.CommandID
        packet.StateFlags = 0x0004
        packet.Data = self.CreateRequest()
        
        # send to client
        responsePacket = adsClient.SendAndRecv(packet)
        
        # check for error
        if (responsePacket.ErrorCode > 0):
            raise AdsException(responsePacket.ErrorCode)
        
        # return response object
        result = self.CreateResponse(responsePacket)
        if (result.Error > 0):
            raise AdsException(result.Error)
        
        return result

        
        
        
