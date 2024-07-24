
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

## Contributing

I welcome contributions to this repository. If you have any improvements, suggestions, or additional scripts that you would like to share, please feel free to open a pull request or submit an issue.

## Contact

If you have any questions or would like to connect, please reach out to me at nchatharoo@icloud.com.

Thank you for visiting my repository. I am excited to continue my journey in cybersecurity and look forward to sharing more scripts and knowledge in the future.
