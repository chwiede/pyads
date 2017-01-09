#!/usr/bin/python2

from pyads import *  

with AdsDevice(amsTarget="192.168.50.107.1.1:800") as device:
    
    # read a global variable from sps
    boolean_value = device.ReadByName(".bMyValue")

    # toggle value, write back
    boolean_value = not boolean_value
    device.WriteByName(".bMyValue", AdsDatatype.Bool, boolean_value)