# Net Sniffer

Net Sniffer is a lightweight, terminal-first packet inspection utility implemented in Python with Scapy. It’s designed for network troubleshooting, learning, and quick diagnostics — showing packet headers, protocols, and basic payload context for traffic observed on a selected interface. The tool focuses on readable, actionable output so you can follow connections, observe DNS and HTTP requests, and spot obvious anomalies without leaving your shell.

# Key features (Currently)

Live capture on a user-specified interface.

Human-friendly output: concise packet summaries (timestamp, src → dst, protocol, ports, length).


# Installation

### Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# or directly
pip install scapy

# Starting Program on Different OS

#### Linux
1. Navigate to your directory where the file is located in your terminal
2. Use the command: 
    - "chmod +x netsniffer.py"
3. Execute program using the command: 
    - "sudo python ./netfniffer.py" or "sudo ./netsniffer.py"

#### Windows
1. Navigate to your directory of where the file is located
2. Open file using "administrator" mode for your terminal - PowerShell or CMD
3. In your terminal execute the following command:
    - "python .\netsniffer"

#### MacOS
1. Navigate to your directory of where you downloaded the program in your terminal
2. Execute the following command:
    - "chmod +x netniffer.py"
3. Start the program using following command:
    - "sudo python ./netsniffer.py" or "sudo ./netsniffer.py"
    

