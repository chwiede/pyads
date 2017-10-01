
class ProcImage:


    def __init__(self, indexGroup, indexOffset, length):
        self.IndexGroup = indexGroup
        self.IndexOffset = indexOffset
        self.Length = length


    IndexGroup = 0

    IndexOffset = 0

    Length = 0

    ByteBuffer = None


    def Read(self, adsClient):
        readResult = adsClient.Read(self.IndexGroup, self.IndexOffset, self.Length)
        self.ByteBuffer = readResult.CreateBuffer()


    def Write(self, adsClient):
        writeData = self.ByteBuffer.raw
        adsClient.Write(self.IndexGroup, self.IndexOffset, writeData)
