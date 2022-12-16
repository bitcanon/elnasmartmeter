#!/usr/bin/env python3
from elna import smartmeter

hostname = '192.168.1.123'

meter = smartmeter.Setup(hostname)

def main():
    ''' Simple menu system allowing for controlling the alarm system. '''

    info = meter.get_info()
    print(f"-----------------------------------------------")
    print(f"          Elna SmartMeter Information")
    print(f"-----------------------------------------------")
    print(f" ID           : {info.id}")
    print(f" Manufacturer : {info.manufacturer}")
    print(f" Model        : {info.model}")
    print(f" Firmware     : {info.firmware}")
    print(f" Hardware     : {info.hardware}")
    print(f" Batch        : {info.batch}")
    print()
    print
    el = meter.get_electricity()
    print(f"-----------------------------------------------")
    print(f"           Elna SmartMeter Readings")
    print(f"-----------------------------------------------")
    print(f" Now      : {el.now.value:7d} {el.now.unit:4s} ({el.now.timestamp})")
    print(f" Minimum  : {el.minimum.value:7d} {el.minimum.unit:4s} ({el.minimum.timestamp})")
    print(f" Maximum  : {el.maximum.value:7d} {el.maximum.unit:4s} ({el.maximum.timestamp})")
    print(f" Imported : {el.imported.value:7d} {el.imported.unit:4s} ({el.imported.timestamp})")
    print(f" Exported : {el.exported.value:7d} {el.exported.unit:4s} ({el.exported.timestamp})")


if __name__ == '__main__':
    # Execute if run as a script
    main()
