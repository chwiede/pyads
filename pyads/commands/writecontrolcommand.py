import struct
from .adscommand import AdsCommand
from .writecontrolresponse import WriteControlResponse

class WriteControlCommand(AdsCommand):

    def __init__(self, adsState, deviceState, data = b''):
        self.CommandID = 0x0005
        self.AdsState = adsState
        self.DeviceState = deviceState
        self.Data = data


    AdsState = 0
    DeviceState = 0
    Data = b''


    def CreateRequest(self):
        result = struct.pack('<HHI', self.AdsState, self.DeviceState, len(self.Data))
        result += self.Data
        return result


    def CreateResponse(self, responsePacket):
        return WriteControlResponse(responsePacket)
