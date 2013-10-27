import os
import sys

libpath = os.path.dirname(__file__)
if (not libpath in sys.path):
    sys.path.append(libpath)
    
from pyads import *