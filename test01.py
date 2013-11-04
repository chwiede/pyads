#!/usr/bin/python2

import binascii
import time
import struct
from src.pyads import *  
from src.pyads.boxes import *


targetAms = "192.168.50.107.1.1:800"
sourceAms = "192.168.50.106.1.1:801"

connection = AdsConnection(targetAms, sourceAms)

adsDevice = AdsDevice(connection)


print(adsDevice.ReadDeviceInfo())
print(adsDevice.ReadState())



t = time.time()

for i in range(2):
    adsDevice.Read(0xf020, 0, 1)

print("%0.1fms" % ((time.time() - t) / 20.0 * 1000))


for box in adsDevice.GetBoxes():
    print("-> %s" % box)
    print("   Offset %s/%s In/Out" % (box.OffsetIn, box.OffsetOut))
    syms = box.CreateSymbolInfos()
    for sym in syms:
        print("   %s" % sym)


print("ready & bye!")