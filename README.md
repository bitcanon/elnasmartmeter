# Elna SmartMeter Library
Hi and welcome! Click the button below if you enjoy this library and want to support my work. A lot of coffee is consumed as a software developer you know 😁

<a href="https://www.buymeacoffee.com/bitcanon" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

>Needless to say, this is completely voluntary.

## Introduction
A simple library for the E.ON Elna API written in Python 3. Elna is a smart power meter that is plugged in to the HAN (Home Area Network) port of the electricity meter using an RJ12 connector. 

The library is using the built-in API in the Elna device to gather information, about your power consuption, directly from the device itself.

> Elna is based on a device from Net2Grid so it's probably also compatible with more devices from the Net2Grid family. Any feedback is welcome.

## Demo
Here is a small command-line demo application showing the information that can be obtained by the library.

![SmartMeter CLI Demo](https://github.com/bitcanon/visonicalarm/blob/master/docs/img/demo-cli-application.gif)

Check out the source code to the demo here: [smartmeter-demo.py](https://github.com/bitcanon/elnasmartmeter/blob/master/examples/smartmeter-demo.py).

## Installation
Install the latest version with `pip`:
```
pip install elnasmartmeter
```

## Basics
### Setup
In order to use the library you need to know the IP address of the Elna device. You can find it in the DHCP server of your router (or wherever you are running your DHCP server). The MAC address is printed on the back of the Elna device.

```python
from elna import smartmeter

# Connect the library to the Elna device
meter = smartmeter.Connect('192.168.1.123')

# Get general information
info = meter.get_info()

# Get power readings
electricity = meter.get_electricity()
```
It's as simple as that to fetch the power consuption of your household. In a moment we will be looking at how to access the information.

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

As an example, you can output the properties of a user object by passing it to the `print()` method:
```python
print(info)
# Output: <class 'elna.classes.Information'>: {'id': '01ab:0200:00cd:03ef', 'manufacturer': 'NET2GRID', 'model': 'SBWF4602', 'firmware': '1.7.14', 'hardware': 1, 'batch': 'HMX-P1D-220921'}
```
Also, the properties are easily accessed from the object:
```python
print(f"Model    : {info.model}")
print(f"Firmware : {info.firmware}")
```
The same goes for all object classes in the library: `Information`, `Electricity` and `Power`.

## Access the Data
There are two pieces of data that can be fetched with this library: general device `information` and `power` usage statistics.

### Device Information
To get the general device information we just call the `get_info()` method.

```python
info = meter.get_info()
```
Access the values via the class properties:
```python
info.id
info.manufacturer
info.model
info.firmware
info.hardware
info.batch
```
### Power Readings
The get the power readings we call the `get_electricity()` method. These readings are a bit more complex since the information gathered from the Elna device is divided in to sub-classes, but it's not that complicated:

```python
electricity = meter.get_electricity()
```

#### Now
Current power consumption.

#### Min
Lowest recorded power..


