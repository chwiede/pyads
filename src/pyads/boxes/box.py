from boxtype import BoxType

class Box():
    
    def __init__(self, descriptor = 0):
        
        # maybe it's a simple digital box?
        isDigitally = (descriptor & 0x8000) != 0
        if (isDigitally):
            if ((descriptor & 0x0001) != 0):
                self.BoxType = BoxType.DigitallyInput
            elif ((descriptor & 0x0002) != 0):
                self.BoxType = BoxType.DigitallyOutput
                
            self.BitLength = (descriptor >> 8) & 0x003F
        
        else:
            self.BoxType = BoxType.Complex                 
            self.Descriptor = descriptor
        
    
    Descriptor = 0
    BitLength = 0
    BoxType = BoxType.Unkown
    
    
    def __str__(self):
        
        result = ''
        
        if (self.BoxType == BoxType.Unkown):
            result += "Unkown Device"
        
        if (self.BoxType == BoxType.Complex):
            result += "Complex Box %s" % self.Descriptor            

        if (self.BoxType == BoxType.DigitallyInput):
            result += "Digital Input, %s Channels" % self.BitLength            

        if (self.BoxType == BoxType.DigitallyOutput):
            result += "Digital Output, %s Channels" % self.BitLength
            
        return result;           
    