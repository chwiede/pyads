from boxtype import BoxType

class Box():
    
    def __init__(self, descriptor = 0):
        self.Descriptor = descriptor        
        self.BoxType = BoxType.GetBoxType(descriptor)
        
        
    Offset = 0        
    
    ByteSize = 0

    Descriptor = 0
    
    BoxType = BoxType.Unkown
    
    
    @property
    def IsComplex(self):
        return (self.BoxType & 0b10000100) == 0b00000100
    
    
    @property
    def IsDigital(self):
        return (self.BoxType & 0b10001000) == 0b00001000
    

    @property
    def IsInput(self):
        return (self.BoxType & 0b10000001) == 1
        
    
    @property
    def IsOutput(self):
        return (self.BoxType & 0b10000010) == 2

        
    
    def __str__(self):
        
        generalType = "Unkown"
        
        if (self.IsComplex):
            generalType = "Complex"
        
        if (self.IsDigital):
            generalType = "Digital"
            
        ioMode = "InOut"
        
        if (self.IsInput and not self.IsOutput):
            ioMode = "In"             

        if (self.IsOutput and not self.IsInput):
            ioMode = "Out"             

        humanDescription = "%s %s" % (generalType, ioMode)
        
        return "Box %s (%s, %s %s)" % (
            self.Descriptor,
            humanDescription,
            self.ByteSize,
            "Bytes" if (self.IsComplex) else "Channels"
        )
