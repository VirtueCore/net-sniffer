#!/bin/python
"""Capture network packets from NIC"""
# Coder: Orient Manning (VirtueCore)

# Import module
from scapy.all import sniff, wrpcap

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
    interface = input("👨🏻‍💻 Enter network interface (i.e. wlan, ethernet): ")

    # Ask use for IP address
    ip_ask = input("🖥️ Enter IP address: ")

    try:
        # Sniff IP address and number of packets to capture
        packets = sniff(
            iface=interface,
            filter=f"host {ip_ask}",
            count=0,
            prn=lambda x: x.show()
            )
        return packets

    except PermissionError:
        print("🔑 You must run this program as root/administrator.")
        return None

    except OSError:
        print("⚠️ Invalid interface or capture error")
        return None


# Function for PCAP file
def save_pcap(packets):
    """Saving results to a PCAP file"""

    # No packets
    if not packets:
        print("🚫 No packets were captured.")

    # Saved Packets File
    filename = "packet.pcap"

    # Store or overwrite packets
    add_packets = input("""
        Would you like to save packets along with old captured packets?
        (Yes or No)
        """).title()

    if add_packets == "Yes":
        # Don't overwrite
        wrpcap(filename, packets, append=True)
    else:
        wrpcap(filename, packets)

    # Information to user
    print(f"\nYour packets are saved in {filename}.💾")


# Main function
def main():
    """Show an exit message"""
    try:
        # Assign network function to a variable
        captured_packets = network()

        # Call PCAP function
        save_pcap(captured_packets)

    # Keyboard interruption
    except KeyboardInterrupt:
        # Exit message
        print("\n🤝 Thanks for using Net Sniffer!")


# Call main Function
if __name__ == '__main__':
    main()
