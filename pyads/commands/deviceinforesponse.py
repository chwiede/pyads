import struct
from .adsresponse import AdsResponse

class DeviceInfoResponse(AdsResponse):
    
    def __init__(self, responseAmsPacket):
        AdsResponse.__init__(self, responseAmsPacket)
        
        self.MajorVersion = struct.unpack_from('B', responseAmsPacket.Data, 4)[0]
        self.MinorVersion = struct.unpack_from('B', responseAmsPacket.Data, 5)[0]
        self.Build = struct.unpack_from('H', responseAmsPacket.Data, 6)[0]
        self.DeviceName = responseAmsPacket.Data[8:].decode("ascii").strip(' \t\n\r\x00')
        
        
    MajorVersion = 0
    
    MinorVersion = 0
    
    Build = 0
    
    DeviceName = 'Ads Device'
    
    
    def __str__(self):
        return "%s (Version %s)" % (self.DeviceName, self.Version())
    
    
    def Version(self):
        return "%s.%s.%s" % (self.MajorVersion, self.MinorVersion, self.Build)               

