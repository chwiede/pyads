from box import Box

class Box2512(Box):
    
    def __init__(self, descriptor):
        Box.__init__(self, descriptor)
        self.ByteSize = 8


    def __str__(self):
        return "KL2512 PWM-Output (2 Channels)"