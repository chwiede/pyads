#!/usr/bin/python2

import binascii
import ctypes
import time
from src.pyads import *  
from src.pyads.boxes import *

targetAms = "192.168.50.107.1.1:800"
sourceAms = "192.168.50.106.1.1:801"



ads = AdsDevice(AdsConnection(targetAms, sourceAms))

# ==================================


var1 = SymbolInfo("Schalter1", 0, 8, AdsDatatype.Bool, 0)
var2 = SymbolInfo("Lampe1", 0, 8, AdsDatatype.Bool, 0)


# ==================================


procOut = ProcessImage(0xF030, 32)
procOut.Read(ads)

procIn = ProcessImage(0xF020, 32)
procIn.Read(ads)


print var2.ReadFrom(procIn.ByteBuffer)


ads.Close()