#!/usr/bin/env python

from pyads import AdsDevice, SymbolInfo, AdsClient, AdsDatatype, AdsIO

with AdsDevice(amsTarget="192.168.50.107.1.1:800") as device:

    # create ads io device...
    io = AdsIO(device)

    # register some variables...
    variables = {"switch": ".bSwitch",
                 "light": ".bLight"}

    for key in variables:
        value = variables[key]
        handle = device.GetSymbolHandle(value)
        io.Register(SymbolInfo(key, 0xf005, handle, AdsDatatype.Bool, 0))

    # and initialize
    io.Initialize()

    # map input "switch" cyclic to output "light"
    while 1:
        io.ReadAll()
        io.Set("light", io.Get("switch"))
        io.WriteAll()
