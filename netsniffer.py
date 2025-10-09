#!/bin/python
"""Capture network packets from NIC"""

# Import module
from scapy.all import sniff

# Program name

NET_SNIFFER = r"""
 _______          __      _________      .__  _____  _____
 \      \   _____/  |_   /   _____/ ____ |__|/ ____\/ ____\___________
 /   |   \_/ __ \   __\  \_____  \ /    \|  \   __\\   __\/ __ \_  __ \
/    |    \  ___/|  |    /        \   |  \  ||  |   |  | \  ___/|  | \/
\____|__  /\___  >__|   /_______  /___|  /__||__|   |__|  \___  >__|
        \/     \/               \/     \/                     \/
"""
print(NET_SNIFFER)


# Network Function
def network():
    """Perform network sniffing program code"""
    # Get network interface
    get_netinf = input("👨🏻‍💻 Enter network interface (i.e. wlan, ethernet): ")

    # Ask use for IP address
    ip_ask = input("🖥️ Enter IP address: ")

    try:
        # Sniff Network Interface and display detail information
        sniff(iface=get_netinf, prn=lambda x: x.show())

        # Sniff IP address and number of packets to capture
        net_sniff = sniff(ip_ask, count=0, verbose=True)

    except PermissionError:
        print("🔑 You must run this program as root/administrator.")

    else:
        # Getting packets information
        print(net_sniff)


# CTRL+C Function to end program
def ctrl_c():
    """Show an exit message"""
    try:
        # Call function
        network()
    except TypeError:
        # Exit message
        print("\n🤝 Thanks for using Net Sniffer!")


# Call CTRL+C Function
ctrl_c()
