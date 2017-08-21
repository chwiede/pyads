pyads
=====

Pyads is a pure python implementation for Beckhoff ADS protocol.
You can send typical ADS-commands like read/write over TCP/IP.
No other libraries (or TwinCAT on Windows) are needed.

Twincat and ADS are developed by Beckhoff (http://www.beckhoff.de). I'm not affiliated in any way.

Pyads does not contain an ADS-router - it's designed for a direct client-server connection.

It supports Python 2.6+ and Python 3.

### Installation by hand

```
git clone git://github.com/chwiede/pyads.git
cd pyads
python setup.py install --optimize=1
```

### Installation on Arch Linux

```
yaourt -S python-pyads
```

## Usage

First of all you need to define source and target AMS-ID connection strings containing the ID and the Port.
An AMS-ID is a free 6-byte long identifier. Mostly IP is contained. See Beckhoff Spec's for more information about.

__Remember: You have to insert your client AMS-ID into the ams table of your target device!__


### First Contact

```python

from pyads import *  

with AdsDevice(amsTarget="192.168.1.79.1.1:800") as device:
    info = device.ReadDeviceInfo()
    print(info)

```

