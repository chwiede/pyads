from boxtype import BoxType

class Box():
    
    def __init__(self, descriptor = 0):
        self.Descriptor = descriptor        
        self.BoxType = BoxType.GetBoxType(descriptor)
        
    
    ByteSize = 0

    Descriptor = 0
    
    BoxType = BoxType.Unkown
        
    
    def __str__(self):
        return "Box %s" % self.Descriptor
