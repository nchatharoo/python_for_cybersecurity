from scapy.all import IP, ICMP, sr1
import socket

def ping_ip(ip):
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=1, verbose=0)  
    return resp is not None 

def port_scan(ip):
    ports = [21, 22, 23, 25, 80, 443, 8000, 8080]
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        try:
            result = sock.connect_ex((ip, port))
            if result == 0: 
                open_ports.append(port)
        except socket.error:
            pass
        finally:
            sock.close()
    
    return open_ports

def scan_network():
    network_prefix = '10.10.30.'

    print("Scanning the network range 10.10.30.0 to 10.10.30.255...")

    for i in range(0, 256):
        ip = network_prefix + str(i)
        if ping_ip(ip):
            print(f"{ip} is up")
            open_ports = port_scan(ip)
            for port in open_ports:
                print(f"-> Port {port} open")

if __name__ == '__main__':
    scan_network()
