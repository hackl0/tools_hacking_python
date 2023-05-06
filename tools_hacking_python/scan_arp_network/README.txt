ARP Scanner

    This Python script performs an ARP scan on a network using Scapy library. It sends an ARP request to a range of IP addresses to discover the MAC addresses of active hosts.

Requirements

    using the command "pip install -r requirements.txt"

Usage

    1 - Run the script using the command "sudo python3 scan_arp_network.py -i <interface> -r <range target> -m <broadcast>". Note that root privileges are required to send ARP requests.
    
    2 - The script will send an ARP request to each IP address in the specified range and print the MAC address and IP address of any active hosts.

Example

    sudo python3 scan_arp_network.py -i eth0 -r 192.168.1.0/24

Notes

    The timeout parameter in srp() sets the maximum time to wait for a response (in seconds).
    The inter parameter in srp() sets the time to wait between sending each packet (in seconds).
    This script is intended for educational and ethical purposes only. Do not use it to scan networks without proper authorization.
