# Elna SmartMeter Library
Hi and welcome! Click the button below if you enjoy this library and want to support my work. A lot of coffee is consumed as a software developer you know 😁

<a href="https://www.buymeacoffee.com/bitcanon" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

>Needless to say, this is completely voluntary.

## Introduction
A simple library for the [E.ON Elna](https://www.eon.se/kundservice/vara-tjanster/e-on-elna) API written in Python 3. Elna is a smart power meter that is plugged in to the HAN (Home Area Network) port of the electricity meter using an RJ12 connector. 

This library is using the built-in API in the Elna device to gather information, about your power **consumption** and/or **production**, directly from the device itself.

> Elna is based on hardware from Net2Grid so it's probably also compatible with more devices from the Net2Grid family. Any feedback is welcome.

## Demo
Here is a small command-line demo application showing the information that can be obtained by the library.

![SmartMeter CLI Demo](https://github.com/bitcanon/elnasmartmeter/blob/main/docs/img/elna-cli-application.gif)

Check out the source code to the demo here: [smartmeter-demo.py](https://github.com/bitcanon/elnasmartmeter/blob/master/examples/smartmeter-demo.py).

## Installation
Install the latest version with `pip`:
```
pip install elnasmartmeter
```

## Basics
### Setup
In order to use the library you need to know the IP address of the Elna device. You can find it in the DHCP server of your router (or wherever you are running your DHCP server). The MAC address of Elna is printed on the back of the device.

```python
from elna import smartmeter

# Connect the library to the Elna device
meter = smartmeter.Connect('192.168.1.123')

# Get general information
info = meter.get_info()

# Get power readings
electricity = meter.get_electricity()
```
It's as simple as that to fetch the power consuption/production of your household. In a moment we will be looking at how to access the information via the `info` and `electricity` objects.

### Exceptions
All of the methods callable from the library will throw exceptions on failure. A full list of exceptions can be found [here](https://github.com/bitcanon/elnasmartmeter/blob/master/elnasmartmeter/exceptions.py).
```python
from elna import smartmeter
from elna.exceptions import *
...
try:
    info = meter.get_info()
except NewConnectionError as e:
    print(e)
```

### Printing Objects and Properties
The objects representing various entities in the library can be output with the `print()` method for easy inspection of its properties.

As an example, you can output the properties of an `Information` object by passing it to the `print()` method:
```python
print(info)
# Output: <class 'elna.classes.Information'>: {'id': '01ab:0200:00cd:03ef', 'manufacturer': 'NET2GRID', 'model': 'SBWF4602', 'firmware': '1.7.14', 'hardware': 1, 'batch': 'HMX-P0D-123456'}
```
Also, the properties are easily accessed from the object:
```python
print(f"Model    : {info.model}")
print(f"Firmware : {info.firmware}")
```
The same goes for all object classes in the library: `Information`, `Electricity` and `Power`.

## Access the Data
There are two pieces of data that can be fetched with this library: general device `Information` and `Power` statistics.

### Device Information
To get the general device information we just call the `get_info()` method.

```python
info = meter.get_info()
```
Access the values via the class properties:
```python
info.id                         # Returns the device ID        : '01ab:0200:00cd:03ef'  (for example).
info.manufacturer               # Returns the manufacturer     : 'NET2GRID'
info.model                      # Returns the model            : 'SBWF4602'
info.firmware                   # Returns the firmware version : '1.7.14'
info.hardware                   # Returns the hardware version : 1
info.batch                      # Returns the batch number     : 'HMX-P0D-123456'
```
### Power Readings
To get the power readings we call the `get_electricity()` method. These readings are a bit more complex since the information gathered from the Elna device is divided in to sub-classes, but it's not that complicated:

```python
electricity = meter.get_electricity()
```

#### Now
Get the **current** power consumption:
```python
electricity.now.key             # Returns the string  : 'now'
electricity.now.value           # Returns the power   : 453  (for example).
electricity.now.unit            # Returns the unit    : 'W'  (as in Watt)
electricity.now.timestamp       # Returns a timestamp : '2022-12-24 13:37:00'
```

#### Minimum
Get the **minimum** power consumption in the period:
```python
electricity.minimum.key         # Returns the string  : 'minimum'
electricity.minimum.value       # Returns the power   : 202  (for example).
electricity.minimum.unit        # Returns the unit    : 'W'  (as in Watt)
electricity.minimum.timestamp   # Returns a timestamp : '2022-12-13 13:37:00'
```

#### Maximum
Get the **maximum** power consumption in the period:
```python
electricity.maximum.key         # Returns the string  : 'maximum'
electricity.maximum.value       # Returns the power   : 14320  (for example).
electricity.maximum.unit        # Returns the unit    : 'W'  (as in Watt)
electricity.maximum.timestamp   # Returns a timestamp : '2022-12-31 13:37:00'
```
> The time frame (period) of which the **minimum** and **maximum** values has been recorded is unknown (to me).

#### Imported
Get the **imported** power. This would be total power coming **into** the household:
```python
electricity.imported.key         # Returns the string  : 'imported'
electricity.imported.value       # Returns the power   : 12345678  (for example).
electricity.imported.unit        # Returns the unit    : 'Wh'  (as in Watt hours)
electricity.imported.timestamp   # Returns a timestamp : '2022-12-31 13:37:00'
```

#### Exported
Get the **exported** power. This would be total power coming **out of** the household:
```python
electricity.exported.key         # Returns the string  : 'exported'
electricity.exported.value       # Returns the power   : 87654321  (for example).
electricity.exported.unit        # Returns the unit    : 'Wh'  (as in Watt hours)
electricity.exported.timestamp   # Returns a timestamp : '2022-12-31 13:37:00'
```
> Check out the smartmeter demo at the top to try it out.

## Legal Disclaimer

The product names, trademarks and registered trademarks in this repository, are property of their respective owners, and are used by the author for identification purposes only. The use of these names, trademarks and brands, do not imply endorsement or affiliation.


