from box import Box
from boxtype import BoxType

class BoxDigital(Box):
    
    def __init__(self, descriptor):
        Box.__init__(self, descriptor)
        self.Channels = BoxType.GetChannelCount(descriptor)
        self.ByteSize = BoxType.GetBoxBitLength(descriptor)  
        
        
    Channels = 0
    
    
    def __str__(self):        
        mode = "Input" if BoxType.GetBoxIsInput(self.Descriptor) else "Output"        
        return "Digital %s Box (%s Channels)" % (mode, self.Channels)        
    
    