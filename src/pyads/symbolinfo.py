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
    
    
    def WriteDown(self, processImage, value):
        
        AdsDatatype.PackInto(value, self.AdsDatatype, processImage, self.IndexOffset)
                
        