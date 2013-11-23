#!/usr/bin/python2

from pyads import *  

with AdsDevice(amsTarget="192.168.50.107.1.1:800") as device:
    
    # create ads io device, register some variables and initialize
    io = AdsIO(device)    
    io.Register(SymbolInfo("switch", AdsClient.AdsIndexGroupIn, 8, AdsDatatype.Bool, 0))
    io.Register(SymbolInfo("light", AdsClient.AdsIndexGroupOut, 8, AdsDatatype.Bool, 0))
    io.Initialize()
    
    # map input "switch" cyclic to output "light" 
    while 1:
        io.ReadAll()
        io.Set("light", io.Get("switch"))       
        io.WriteAll()        
