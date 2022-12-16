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
In order to use the library you need to know the IP address of the Elna device. This is most easily found in the DHCP server of your router (or wherever you are running your DHCP server).

```python
from elna import smartmeter

# Connect the library to the Elna device
meter = smartmeter.Connect('192.168.1.123')

# Get general information
info = meter.get_info()

# Get power readings
electricity = meter.get_electricity()
```
It's as simple as that to fetch the power consuption of your household. Next we will be looking at how to access the information.

### Exceptions
All of the methods callable from the library will throw exceptions on failure. A full list of exceptions can be found [here](https://github.com/bitcanon/visonicalarm/blob/master/visonic/exceptions.py).
```python
from visonic.exceptions import *
...
try:
    alarm.panel_login(panel_serial, user_code)
except UserCodeIncorrectError as e:
    print(e)
```

### Printing Objects and Properties
The objects representing various entities in the alarm system can be output with the `print()` method for easy inspection of its properties.

As an example, you can output the properties of a user object by passing it to the `print()` method:
```python
print(user)
# Output: <class 'visonic.classes.User'>: {'id': 1, 'name': 'John Doe', 'email': 'john@doe.com', 'partitions': [1, 2, 3, 4, 5]}
```
Also, the properties are easily accessed from the object:
```python
print('User ID:    ' + str(user.id))
print('User Name:  ' + user.name)
print('Email:      ' + user.email)
print('Partitions: ' + str(user.partitions))
```
This is the same for all object classes in the library: Users, devices, events, locations, troubles, and so on...

## Arming and Disarming
There are two ways to arm your alarm system.
- **Arm Home:** This will arm your perimeter protection (often doors and windows). You can still move around inside the house.
- **Arm Away:** This will arm the entire alarm system (doors, windows, motion, cameras, etc). Moving around in the house will trigger the alarm to go off.

### Arm Home
To arm the alarm system in *home mode* just call the `arm_home()` method. 

```python
alarm.arm_home()
```
When using a multi partition alarm system, just pass the partition ID as an argument to the `arm_home()` method.
```python
alarm.arm_home(partition=2)
```

Poll the `state` property of your partition in the `get_status()` method to watch the state changing.
```python
alarm.get_status().partitions[0].state  # Output: 'HOME'
```
