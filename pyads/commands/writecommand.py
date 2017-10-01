import struct
from .adscommand import AdsCommand
from .writeresponse import WriteResponse

class WriteCommand(AdsCommand):

    def __init__(self, indexGroup, indexOffset, data):
        self.CommandID = 0x0003
        self.IndexGroup = indexGroup
        self.IndexOffset = indexOffset
        self.Data = data



    IndexGroup = 0

    IndexOffset = 0

    Data = b''


    def CreateRequest(self):
        result = struct.pack('<III', self.IndexGroup, self.IndexOffset, len(self.Data))
        result += self.Data
        return result


    def CreateResponse(self, responsePacket):
        return WriteResponse(responsePacket)
