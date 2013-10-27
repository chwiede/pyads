pyads
=====

Pyads is a pure python implementation for Beckhoff ADS protocol.
You can send typical ADS-commands like read/write over TCP/IP.
No other libraries (or TwinCAT on Windows) are needed.

./src/pyads is the main library folder. Copy or add it to your systems python library path.

## Usage

First of all you need to define source and target AMS-ID connection strings containing the ID and the Port.
An AMS-ID is a free 6-byte long identifier. Mostly IP is contained. See Beckhoff Spec's for more information about.

### First Contact

```python

import pyads

sourceAmsIdPort = "192.168.1.79.1.1:32780"
targetAmsIdPort = "192.168.1.80.1.1:801"

connection = AdsConnection(targetAmsIdPort, sourceAmsIdPort)
adsClient = AdsClient(connection)

deviceInfo = adsClient.ReadDeviceInfo()

print(deviceInfo)

adsClient.Close()

```

