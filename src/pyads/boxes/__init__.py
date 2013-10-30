
__all__ = [
    "box", 
    "boxdigital", 
    "boxtype"
]

from box import Box
from boxtype import BoxType
from boxdigital import BoxDigital

def Create(descriptor):
    
    # return digital, if is
    if(BoxType.GetBoxIsDigital(descriptor)):
        return BoxDigital(descriptor)
    
    # return complex, if implemented
    # TODO
    
    # return base class
    return Box(descriptor)    