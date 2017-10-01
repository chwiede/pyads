__all__ = [
    "AdsClient",
    "AdsConnection",
    "AdsDatatype",
    "AdsDevice",
    "AdsException",
    "AdsState",
    "amspacket",
    "AmsPacket",
    "BinaryParser",
    "SymbolInfo",
    "HexBlock",
    "AdsIO",
    "ProcImage"
]

from pyads.symbolinfo import *
from pyads.adsdatatype import *
from pyads.adsexception import *
from pyads.adsstate import *
from pyads.amspacket import *
from pyads.binaryparser import *
from pyads.adsconnection import *
from pyads.adsclient import *
from pyads.adsdevice import *
from pyads.adsio import *
from pyads.procimage import *


def HexBlock(data, width = 8):
    i, result, currentHexLine, currentChrLine = 0, '', '', ''

    for byte in data:

        # next line, if required
        if (i == width):
            result += '%s %s\n' % (currentHexLine, currentChrLine)
            currentHexLine = ''
            currentChrLine = ''
            i = 0

        # python2 / python3 - normalize to numeric byte
        char = ord(byte) if isinstance(byte, str) else byte

        # append to lines
        currentHexLine += '%02x ' % char
        currentChrLine += '.' if (char < 32 or char > 126) else chr(char)
        i += 1

    # append last line
    result += '%s %s' % (currentHexLine, currentChrLine)
    return result