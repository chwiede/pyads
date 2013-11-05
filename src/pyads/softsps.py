import time
from adsdevice import AdsDevice, AdsClient

class SoftSPS:
    
    def __init__(self, adsConnection):
        self.AdsDevice = AdsDevice(adsConnection)
    
    
    SymbolInfos = {}
    
    CycleTime = 0.0
    
    Running = False
    
    AdsDevice = None    
    
    ProcessImgIn = None
    
    ProcessImgInLength = 512
    
    ProcessImgOut = None

    ProcessImgOutLength = 512
    
    
    def ReadProcessImgIn(self):
        self.ProcessImgIn = self.AdsDevice.Read(
            AdsClient.AdsIndexGroupIn, 
            0, 
            self.ProcessImgInLength
        ).CreateBuffer()

    
    
    def ReadProcessImgOut(self):
        self.ProcessImgOut = self.AdsDevice.Read(
            AdsClient.AdsIndexGroupOut, 
            0, 
            self.ProcessImgInLength
        ).CreateBuffer()
    
    
    
    def WriteProcessImgOut(self):
        self.AdsDevice.Write(AdsClient.AdsIndexGroupOut, 0, self.ProcessImgOut.raw)
        
        
    
    def CreateVariables(self):
        boxes = self.AdsDevice.GetBoxes()
        for i in range(1, len(boxes)):
            symbolInfos = boxes[i].CreateSymbolInfos()
            for symbolInfo in symbolInfos:
                symbolName = "box%s_%s" % (i, symbolInfo.Name)
                self.SymbolInfos[symbolName] = symbolInfo
                
                    

    def Loop(self, callback):
        
        # set flag
        self.Running = True        
        
        # read output image
        self.ReadProcessImgOut()
        
        # enter main loop
        while self.Running:
            
            # measure time, read inputs
            timeStart = time.time()
            self.ReadProcessImgIn()
            
            # map variables
            #for sym in self.SymbolInfos.itervalues():
            #    if (sym.IndexGroup == AdsClient.AdsIndexGroupIn):
            #        sym.ReadFrom(self.ProcessImgIn) 
            
            # logic
            callback(self)
            
            # write outputs
            self.WriteProcessImgOut()
            
            # define sleep and wait
            sleep = max(0, self.CycleTime - (time.time() - timeStart))
            time.sleep(sleep)


    
    def __getattr__(self, name):
        return self.SymbolInfos[name].Value
        
    
    def __setattr__(self, name, value):
        self.SymbolInfos[name].Value = value
    
    
    def Close(self):
        
        self.Running = False
        
        if (self.AdsDevice != None):
            self.AdsDevice.Close()