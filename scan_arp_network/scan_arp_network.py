import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description='ARP scan tool')
parser.add_argument('-i', '--interface', type=str, help='Network interface', required=True)
parser.add_argument('-r', '--range', type=str, help='IP range to scan', required=True)
parser.add_argument('-m', '--broadcast', type=str, help='Broadcast MAC address', default='ff:ff:ff:ff:ff:ff')

args = parser.parse_args()

packet = Ether(dst=args.broadcast) / ARP(pdst=args.range)

ans, unans = srp(packet, timeout=2, iface=args.interface, inter=0.1)

for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
