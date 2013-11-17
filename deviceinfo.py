#!/usr/bin/python2

from pyads import *  


with AdsDevice(amsTarget="192.168.50.107.1.1:800") as device:
    print device
    info = device.ReadDeviceInfo()
    print(info)
