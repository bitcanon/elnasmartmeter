#!/usr/bin/env python3
from random import randrange
from socket import gethostbyname, gaierror
from time import sleep, perf_counter

from elna import smartmeter
from elna.exceptions import NewConnectionError

def main():
    ''' Power ping demo application. '''

    # Hostname or IP address of Elna
    elna_host = 'elna.example.com'

    # Send and received HTTP packets
    elna_tx = 0
    elna_rx = 0

    # Momentary Power Consumption (mpc) statistics
    mpc_min = 0
    mpc_max = 0
    mpc_avg = 0

    # Round Trip Time (rtt) statistics
    rtt_min = 0
    rtt_max = 0
    rtt_avg = 0

    # Power ping started timestamp
    exec_start = perf_counter()

    # IP address of Elna is automatically resolved (DO NOT MODIFY)!
    elna_ip = None
    try:
        elna_ip = gethostbyname(elna_host)
    except gaierror as e:
        print(f"powerping: {elna_host}: {e.args[1]}")
        return 0

    # Setup the library connection
    meter = smartmeter.Connect(elna_ip)

    # Only for demo output (hide real address information)
    # elna_host = 'elna.example.com'
    # elna_ip = '192.168.0.10'

    # Ping until the user presses Ctrl+C
    print(f"POWER PING {elna_host} ({elna_ip}). Terminate with CTRL+C.")
    while True:
        try:
            # Add a slight randomness for effect (Elna only updates its value once every 10 seconds)
            rand = randrange(-3, 3)

            # Reset the minimum values
            if mpc_min == 0: mpc_min = mpc_max
            if rtt_min == 0: rtt_min = rtt_max

            # Get Elna power reading and time the operation
            try:
                elna_tx += 1
                rtt_start = perf_counter()
                mpc = meter.get_electricity().now.value + rand
                rtt_end = perf_counter()
                elna_rx += 1

                # Calculate the round trip time in seconds
                rtt = rtt_end-rtt_start
                if rtt < rtt_min: rtt_min = rtt
                if rtt > rtt_max: rtt_max = rtt
                rtt_avg += rtt

                # Calculate the momentary power consumption in seconds
                if mpc < mpc_min: mpc_min = mpc
                if mpc > mpc_max: mpc_max = mpc
                mpc_avg += mpc

                # Print the result to console
                print(f"{mpc} watt from {elna_ip}: tcp_seq={elna_tx} time={rtt*1000:0.1f} ms")

                # Try to sleep as close to one seconds as possible until next request
                if rtt > 1: rtt = 0
                sleep(1-rtt)
            except NewConnectionError as e:
                # Connection to Elna failed
                mpc = 0
                print(f"{mpc} watt from {elna_ip}: tcp_seq={elna_tx} Destination Device Unreachable")
                sleep(1)

        except KeyboardInterrupt:
            print()
            break

    # Calculate the total program execution time
    exec_total = perf_counter() - exec_start

    # Print the final ping statistics to console
    print(f"--- {elna_host} ping statistics ---")
    print(f"{elna_tx} packets transmitted, {elna_rx} received, {(elna_tx-elna_rx)/elna_tx*100:.2f}% packet loss, time {exec_total:.2f} sec")

    # Round Trip Time (rtt)
    print(f"rtt min/avg/max = {rtt_min*1000:.3f}/{rtt_avg/elna_tx*1000:.3f}/{rtt_max*1000:.3f} ms")

    # Momentary Power Consupmtion (mpc)
    print(f"mpc min/avg/max = {mpc_min}/{mpc_avg/elna_tx:.0f}/{mpc_max} watt")


if __name__ == '__main__':
    # Execute if run as a script
    main()
