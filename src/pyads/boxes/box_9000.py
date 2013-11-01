from box import Box, BoxType

class Box9000(Box):
    
    def __init__(self, descriptor):
        Box.__init__(self, descriptor)
        self.SizeIn = 8
        self.SizeOut = 8
        self.BoxType = BoxType.Complex | BoxType.Input | BoxType.Output


    def __str__(self):
        return "Bus Coupler BC9000"