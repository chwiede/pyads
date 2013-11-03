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


procOut = ProcessImage(0xF030, 511)
procOut.Read(ads)

procIn = ProcessImage(0xF020, 511)

oldswitch = False
lamp = False

while 1:
    try:        
        
        procIn.Read(ads)
        
        switch = var1.ReadFrom(procIn.ByteBuffer)
        lamp = var2.ReadFrom(procOut.ByteBuffer)
        
        
        if(not oldswitch and switch):
            lamp = not lamp        
        
        oldswitch = switch
        
        
        var2.WriteToBuffer(procOut.ByteBuffer, lamp)
        
        
        procOut.Write(ads)
        
        
        
    except Exception as err:
        print err
        break;


ads.Close()