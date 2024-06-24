
# Python Networking and Cybersecurity Scripts

Welcome to my Python networking and cybersecurity scripts repository! This repository contains a collection of Python scripts that I have developed to enhance my skills and knowledge in the field of cybersecurity. Each script demonstrates fundamental concepts and techniques used in network programming and cybersecurity.

## Scripts Included

1. **TCP Client** (`tcp_client.py`): 
   - A simple TCP client that connects to a specified server, sends data, and receives a response. This script demonstrates basic TCP socket programming and data exchange over a network.

2. **UDP Client** (`udp_client.py`): 
   - A straightforward UDP client that sends data to a specified server and receives a response. This script showcases the use of UDP sockets for lightweight, connectionless communication.

3. **Netcat** (`netcat.py`): 
   - A versatile network utility script inspired by the traditional Netcat tool. This script can be used to read and write data across network connections using the TCP/IP protocol. It supports features such as port listening, command execution, and file transfers.

4. **TCP Server** (`tcp_server.py`): 
   - A basic TCP server that listens for incoming connections, receives data from clients, and sends responses. This script highlights server-side socket programming and handling multiple client connections.

5. **TCP Proxy** (`TCP_proxy.py`):
   - A script that sets up a proxy to forward TCP traffic between a local and a remote host. This proxy can be used for intercepting and modifying traffic for analysis and testing. It includes functions to handle requests and responses, making it useful for understanding and manipulating protocol communications.

6. **SSH Command Execution** (`ssh_cmd.py`):
   - This script uses the Paramiko library to execute commands on a remote server over SSH. It demonstrates how to establish an SSH connection, authenticate, and execute a command on the remote server.

7. **SSH Remote Command Execution** (`ssh_rcmd.py`):
   - This script sets up an SSH connection and allows for the execution of remote commands interactively. It maintains a session to handle multiple commands.

8. **SSH Server** (`ssh_server.py`):
   - This script sets up a simple SSH server using Paramiko that listens for connections, authenticates users, and executes commands sent by the client.

9. **Network Scanner** (`scanner.py`):
   - A network scanner to discover active hosts using UDP packets and listening for ICMP, TCP and UDP responses.

10. **ARP Poisoning** (`arper.py`):
   - A script designed for ARP poisoning attacks. It allows an attacker to intercept and manipulate network traffic between a victim and the gateway, effectively placing the attacker in the middle of the communication stream (man-in-the-middle attack)

## Motivation

I am passionate about learning and growing in the field of cybersecurity. Through these scripts, I aim to deepen my understanding of network protocols, socket programming, and various cybersecurity techniques. This repository serves as a testament to my dedication and motivation to enhance my skills and contribute to the cybersecurity community.

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
- **ARP Table Restoration**: After the attack, the script restores the original ARP tables of the victim and the gateway to avoid detection and network issues.
- Example usage:
  ```
  sudo python arper.py <victim_ip> <gateway_ip> <interface>
  ```

## Contributing

I welcome contributions to this repository. If you have any improvements, suggestions, or additional scripts that you would like to share, please feel free to open a pull request or submit an issue.

## Contact

If you have any questions or would like to connect, please reach out to me at nchatharoo@icloud.com.

Thank you for visiting my repository. I am excited to continue my journey in cybersecurity and look forward to sharing more scripts and knowledge in the future.
