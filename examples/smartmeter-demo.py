#!/usr/bin/env python3
from elna import smartmeter

hostname = '192.168.1.123'

meter = smartmeter.Setup(hostname)

def main():
    ''' Application demo output. '''

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

    el = meter.get_electricity()
    print(f"-----------------------------------------------")
    print(f"           Elna SmartMeter Readings")
    print(f"-----------------------------------------------")
    print(f" Now      : {el.now.value:7d} {el.now.unit:4s} ({el.now.timestamp})")
    print(f" Minimum  : {el.minimum.value:7d} {el.minimum.unit:4s} ({el.minimum.timestamp})")
    print(f" Maximum  : {el.maximum.value:7d} {el.maximum.unit:4s} ({el.maximum.timestamp})")
    print(f" Imported : {el.imported.value:7d} {el.imported.unit:4s} ({el.imported.timestamp})")
    print(f" Exported : {el.exported.value:7d} {el.exported.unit:4s} ({el.exported.timestamp})")
    print()

    wlan = meter.get_wlan_info()
    print(f"-----------------------------------------------")
    print(f"           Elna WLAN Configuration")
    print(f"-----------------------------------------------")
    print(f" Wireless Mode   : {wlan.mode}")
    print(f" AP SSID         : {wlan.ap_ssid}")
    print(f" AP Password     : {wlan.ap_key}")
    print(f" Client SSID     : {wlan.client_ssid}")
    print(f" Join Status     : {wlan.join_status}")
    print()
    print(f" MAC Address     : {wlan.mac}")
    print(f" IP Address      : {wlan.ip}")
    print(f" Subnet Mask     : {wlan.subnet}")
    print(f" Gateway         : {wlan.gateway}")
    print(f" DNS (primary)   : {wlan.dns}")
    print(f" DNS (secondary) : {wlan.dnsalt}")
    print()
    print(f" Net2Grid ID     : {wlan.n2g_id}")
    print(f" Station MAC     : {wlan.sta_mac}")
    print(f" AP MAC          : {wlan.ap_mac}")
    print(f" Ethernet MAC    : {wlan.eth_mac}")
    print()

if __name__ == '__main__':
    # Execute if run as a script
    main()
