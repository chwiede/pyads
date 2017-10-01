import re

class AdsConnection:

    def __init__(self, targetAms='0.0.0.0.0.0:0', sourceAms=None, targetIP=None):

        targetAmsInfo = self.ParseAmsIdPort(targetAms)
        if targetIP is None:
            self.TargetIP = targetAmsInfo[0]
        else:
            self.TargetIP = targetIP
        self.TargetAmsID = targetAmsInfo[1]
        self.TargetAmsPort = targetAmsInfo[2]

        if sourceAms == None:
            sourceAms = self.GetDefaultSourceAms()

        sourceAmsInfo = self.ParseAmsIdPort(sourceAms)
        self.SourceAmsID = sourceAmsInfo[1]
        self.SourceAmsPort = sourceAmsInfo[2]



    def ParseAmsIdPort(self, amsconnection):
        pattern = '([0-9\.]+):([0-9]+){1}'
        match = re.match(pattern, amsconnection)
        if (match == None):
            raise Exception("amsid port format not valid. You must enter i.e. '192.168.1.17.1.1:800'.")

        amsID = str(match.group(1))
        tcpIP = '.'.join(x for x in amsID.split('.')[:4])
        amsPort = int(match.group(2))

        return (tcpIP, amsID, amsPort)



    TargetIP = ''
    TargetAmsID = ''
    TargetAmsPort = 0

    SourceAmsID = ''
    SourceAmsPort = 0


    def GetDefaultSourceAms(self):
        return '0.0.0.0.0.0:32905'


    def __str__(self):
        return "%s:%s --> %s:%s" % (
            self.SourceAmsID,
            self.SourceAmsPort,
            self.TargetAmsID,
            self.TargetAmsPort,
        )
