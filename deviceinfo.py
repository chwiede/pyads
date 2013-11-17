#!/usr/bin/python2

from pyads import *  


targetAms = "192.168.50.107.1.1:800"
sourceAms = "192.168.50.106.1.1:801"

connection = AdsConnection(targetAms, sourceAms)
adsDevice = AdsDevice(connection)

adsDevice.Connect()

print(adsDevice.ReadDeviceInfo())

adsDevice.Close()