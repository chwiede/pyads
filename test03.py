#!/usr/bin/python2

import binascii
import ctypes
import struct
import time
from src.pyads import *  
from src.pyads.boxes import *

targetAms = "192.168.50.107.1.1:800"
sourceAms = "192.168.50.106.1.1:801"

connection = AdsConnection(targetAms, sourceAms)
sps = SoftSPS(connection)


sps.CreateVariables()


def foo(sps):
    sps.box2_channel0 = sps.box3_channel0
    print("tick")



sps.Loop(foo)





sps.Close()
