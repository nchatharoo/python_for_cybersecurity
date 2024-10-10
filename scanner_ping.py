import subprocess
import socket

def ping_ip(ip):
    response = subprocess.run(['ping', "-c", '1', ip])

    return response.returncode == 0

def scan_network():
    network_prefix = '10.10.30.'
    
    print("Scanning the network range...")

    for i in range(0, 256):
        ip = network_prefix + str(i)
        if ping_ip(ip):
            print(f"Active IP: {ip}")
            port_scan(ip)

def port_scan(ip):
    ports = [21, 22, 23, 25, 80, 443, 8000, 8080]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in ports:
        client.connect_ex((ip, port))
        print(f'-> Port {port} open')
    pass

if __name__ == '__main__':
    scan_network()
