import struct
from .adscommand import AdsCommand
from .readresponse import ReadResponse

class ReadCommand(AdsCommand):

    def __init__(self, indexGroup, indexOffset, length):
        self.CommandID = 0x0002
        self.IndexGroup = indexGroup
        self.IndexOffset = indexOffset
        self.Length = length



    IndexGroup = 0

    IndexOffset = 0

    Length = 0


    def CreateRequest(self):
        return struct.pack('<III', self.IndexGroup, self.IndexOffset, self.Length)


    def CreateResponse(self, responsePacket):
        return ReadResponse(responsePacket)