from .procimage import ProcImage
from .adsclient import AdsClient

class AdsIO:


    def __init__(self, client):
        self.Client = client


    Client = None
    ProcImageIn = ProcImage(AdsClient.AdsIndexGroupIn, 0x0000, 512)
    ProcImageOut = ProcImage(AdsClient.AdsIndexGroupOut, 0x0000, 512)

    _Variables = {}


    def Register(self, symbolInfo):
        self._Variables[symbolInfo.Name] = symbolInfo


    def Get(self, symbolName):
        return self._Variables[symbolName].Value


    def Set(self, symbolName, value):
        self._Variables[symbolName].Value = value


    def Initialize(self):
        self.ProcImageOut.Read(self.Client)
        self.ReadVariables(self.ProcImageOut)

        self.ProcImageIn.Read(self.Client)
        self.ReadVariables(self.ProcImageIn)


    def ReadAll(self):
        self.ProcImageIn.Read(self.Client)
        self.ReadVariables(self.ProcImageIn)


    def ReadVariables(self, procImage):
        for si in list(self._Variables.values()):
            if si.IndexGroup == procImage.IndexGroup:
                si.ReadFrom(procImage.ByteBuffer)


    def WriteAll(self):
        self.WriteVariables(self.ProcImageOut)
        self.ProcImageOut.Write(self.Client)


    def WriteVariables(self, procImage):
        for si in list(self._Variables.values()):
            if si.IndexGroup == procImage.IndexGroup:
                si.WriteTo(procImage.ByteBuffer)

