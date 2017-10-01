import struct
from .adscommand import AdsCommand
from .readwriteresponse import ReadWriteResponse

class ReadWriteCommand(AdsCommand):

    def __init__(self, indexGroup, indexOffset, readLen, dataToWrite = b''):
        self.CommandID = 0x0009
        self.IndexGroup = indexGroup
        self.IndexOffset = indexOffset
        self.ReadLen = readLen
        self.Data = dataToWrite



    IndexGroup = 0

    IndexOffset = 0

    ReadLen = 0

    Data = b''


    def CreateRequest(self):
        result = struct.pack('<II', self.IndexGroup, self.IndexOffset)
        result += struct.pack('<II', self.ReadLen, len(self.Data))
        result += self.Data
        return result


    def CreateResponse(self, responsePacket):
        return ReadWriteResponse(responsePacket)
