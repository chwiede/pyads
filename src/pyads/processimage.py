class ProcessImage:
    
    def __init__(self, indexGroup = 0, length = 0):
        self.IndexGroup = indexGroup
        self.Length = length 
        
    
    IndexGroup = 0
    
    Length = 0
    
    ByteBuffer = None    
    
    
    
    def Read(self, adsClient):
        self.ByteBuffer = adsClient.Read(self.IndexGroup, 0, self.Length).CreateBuffer()