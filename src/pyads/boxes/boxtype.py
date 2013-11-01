import math
from mercurial.fileset import unknown

class BoxType():
    
    Complex = 0b00000100
    
    Digital = 0b00001000

    Unkown = 0b10000000
    
    Input = 0b00000001
    
    Output = 0b00000010
    
    
    @staticmethod
    def GetBoxType(descriptor):
        
        if (BoxType.GetBoxIsDigital(descriptor)):
            if (BoxType.GetBoxIsInput(descriptor)):
                return BoxType.Digital | BoxType.Input

            if (BoxType.GetBoxIsOutput(descriptor)):
                return BoxType.Digital | BoxType.Output
        
        return BoxType.Complex


    @staticmethod
    def GetBoxIsDigital(descriptor):
        return (descriptor & 0x8000) != 0
    
    
    @staticmethod
    def GetBoxIsInput(descriptor):
        return (descriptor & 0x0001) != 0


    @staticmethod
    def GetBoxIsOutput(descriptor):
        return (descriptor & 0x0002) != 0
    
    
    @staticmethod
    def GetChannelCount(descriptor):
        if (not BoxType.GetBoxIsDigital(descriptor)):
            raise Exception("Box is not digital!")

        return (descriptor >> 8) & 0x003F           
    
    
    @staticmethod
    def GetBoxBitLength(descriptor):
        channelCount = BoxType.GetChannelCount(descriptor)
        return int(math.ceil(channelCount / 8.0) * 8)
