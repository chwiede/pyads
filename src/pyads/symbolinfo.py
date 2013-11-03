from adsdatatype import AdsDatatype

class SymbolInfo:
    
    
    def __init__(self, name, indexGroup, indexOffset, adsDatatype, bitOffset = 0):
        self.Name = name
        self.IndexGroup = indexGroup,
        self.IndexOffset = indexOffset
        self.AdsDatatype = adsDatatype
        self.BitOffset = bitOffset
    
    
    Name = ''    
    
    IndexGroup = 0
    
    IndexOffset = 0
    
    BitOffset = 0            
    
    AdsDatatype = AdsDatatype.Custom
    
    
    def WriteToBuffer(self, byteBuffer, value):
        
        # byte shift needed, if bool!
        if (self.AdsDatatype == AdsDatatype.Bool):
            currentByte = AdsDatatype.UnPackFrom(AdsDatatype.UInt8, byteBuffer, self.IndexOffset)
            if (value):
                newByte = currentByte | (1 << self.BitOffset)
            else:
                newByte = currentByte & ~(1 << self.BitOffset) & 0xF
                
            AdsDatatype.PackInto(AdsDatatype.UInt8, byteBuffer, self.IndexOffset, newByte)
        
        else:
            AdsDatatype.PackInto(self.AdsDatatype, byteBuffer, self.IndexOffset, value)
                
        