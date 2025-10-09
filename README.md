# Net Sniffer
Net Sniffer is a lightweight, terminal-first packet inspection utility implemented in Python with Scapy. It’s designed for network troubleshooting, learning, and quick diagnostics — showing packet headers, protocols, and basic payload context for traffic observed on a selected interface. The tool focuses on readable, actionable output so you can follow connections, observe DNS and HTTP requests, and spot obvious anomalies without leaving your shell.

# Key features (Currently)

Live capture on a user-specified interface.

Human-friendly output: concise packet summaries (timestamp, src → dst, protocol, ports, length).


Installation
# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# or directly
pip install scapy


