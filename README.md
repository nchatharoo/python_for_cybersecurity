
# Python cybersecurity scripts

Welcome to my Python networking and cybersecurity scripts repository! This repository contains a collection of Python scripts that I have developed to enhance my skills and knowledge in the field of cybersecurity. Each script demonstrates fundamental concepts and techniques used in network programming and cybersecurity.

## Motivation

I am pursuing a career transition into cybersecurity. My goal is to leverage my programming skills and knowledge  to contribute to the field of cybersecurity. This repository serves as a testament to my dedication and motivation to enhance my skills and to prepare myself for a professional role in this exciting and vital domain.

## ⚠️ Important Note ⚠️

Use these scripts only in a controlled environment and with proper authorization. Unauthorized use of these scripts on networks you do not own or have explicit permission to test is illegal and unethical.

## Getting Started

To run any of these scripts, you will need Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Running the Scripts

**Clone the repository**:

   ```git git@github.com:nchatharoo/python_networking.git```
   
   ```cd python_networking```

## Usage

### TCP Client

- Connects to a specified TCP server.
- Sends a message and receives a response.
- Example usage:
  ```
  python3 tcp_client.py
  ```

### UDP Client

- Sends a message to a specified UDP server.
- Receives a response.
- Example usage:
  ```
  python3 udp_client.py
  ```

### Netcat

- A versatile networking tool.
- Can be used to listen on a port, connect to a server, execute commands, and transfer files.
- Example usage:
  ```
  python3 netcat.py -t <target> -p <port> -l -c
  ```

### TCP Server

- Listens for incoming TCP connections.
- Receives data from clients and sends responses.
- Example usage:
  ```
  python3 tcp_server.py
  ```

### TCP Proxy

- Sets up a proxy to forward TCP traffic.
- Can intercept and modify requests and responses for analysis.
- Example usage:
  ```
  sudo python3 TCP_proxy.py local.IP 21 remote.IP 21 True
  ```

### SSH Command Execution

- Executes a command on a remote server over SSH.
- Example usage:
  ```
  python3 ssh_cmd.py
  ```

### SSH Remote Command Execution

- Sets up an SSH connection and allows for interactive remote command execution.
- Example usage:
  ```
  python3 ssh_rcmd.py
  ```

### SSH Server

- Sets up a simple SSH server that listens for connections and authenticates users.
- Example usage:
  ```
  python3 ssh_server.py
  ```

### Network Scanner

- The script sends UDP datagrams with a specific message to all IP addresses in a subnet and listens for ICMP "Destination Unreachable" responses to determine active hosts. It also decodes TCP and UDP packets.
- Example usage:
  ```
  python3 scanner.py
  ```

### ARP poisoning

- The script sends ARP responses to both the victim and the gateway, making them believe that the attacker's MAC address is the one associated with the other's IP address.
- **Packet Sniffing**: The script captures packets from the victim, allowing the attacker to inspect the intercepted traffic.
- **ARP Table Restoration**: After the attack, the script restores the original ARP tables of the victim and the gateway to avoid detection and network issues. You should see an arper.pcap file in the same directory
- Example usage:
  ```
  sudo python arper.py <victim_ip> <gateway_ip> <interface>
  ```

### Email Sniffer

- **Packet Sniffing**: The script captures TCP packets on ports 110 (POP3), 25 (SMTP), and 143 (IMAP).
- **Credential Detection**: It scans the payload of these packets for 'user' or 'pass' keywords, indicating potential usernames and passwords being transmitted.
- **Logging**: When such keywords are found, it logs the destination IP address and the packet payload for further analysis.
- Example usage:
  ```
  sudo python mail_sniffer.py
  ```

### Volatility Memory Image Analysis Tool

This Python script is designed to streamline the process of analyzing memory images using the Volatility framework. It was inspired by challenges on root-me.org, specifically focused on forensic analysis. It allows you to run multiple Volatility plugins on a memory image, analyze the results, and generate an HTML report summarizing the findings.

Requirements

    Volatility: Ensure that Volatility is installed and accessible in your system's PATH.
    Jinja2: For generating the HTML report (pip install jinja2).

Usage
Basic Command

To run the script, use the following command:

bash

python analyze_memory.py <path_to_memory_image>

Command-Line Arguments

    image_file: Path to the memory image file to analyze.
    --output: (Optional) Specify the output HTML report file name. Default is rapport_analyse.html.

Example:

bash

python analyze_memory.py memory.img --output analysis_report.html

Interactive Plugin Selection

After starting the script, you will be prompted to select the plugins you wish to run. You can select them by number or by name.

Example selection:

markdown

1. pslist
2. netscan
3. filescan
...
Enter your selection: 1 3 envars

Output

The script will generate an HTML report that includes:

    Timestamp: When the analysis was performed.
    Host OS: Detected operating system of the host running the script.
    Image OS: Detected operating system of the memory image.
    Plugin Results: Detailed tables showing the output of each selected plugin.

Example Output

Supported Plugins (WIP)

The following plugins are supported with custom analyzers:

    pslist: Process listing.
    netscan: Network connections.
    filescan: File scanning.
    malfind: Malware detection.
    envars: Environment variables.
    handle: Open handles.
    cmdline: Command lines.
    dlllist: Loaded DLLs.
