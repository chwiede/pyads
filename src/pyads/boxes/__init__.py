import os
import imp

__all__ = [
    "box", 
    "boxdigital", 
    "boxtype"
]

import boxtype

from box import Box
from boxtype import BoxType
from boxdigital import BoxDigital

def Create(descriptor):
    
    # return digital, if is
    if(BoxType.GetBoxIsDigital(descriptor)):
        return BoxDigital(descriptor)
    
    # return complex, if implemented
    moduleName = "box_%s" % descriptor
    fileDesired = "%s/%s.py" % (os.path.dirname(__file__), moduleName)
    if (os.path.isfile(fileDesired)):
        module = __import__(moduleName, globals(), locals())
        boxClass = getattr(module, "Box%s" % descriptor)
        return boxClass(descriptor)
    
    
    # return base class
    return Box(descriptor)    