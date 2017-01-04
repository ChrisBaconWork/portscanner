#!/usr/bin/env python3
import socket
from multiprocessing import Pool

def scan(host, ports):
    processor = Pool()
    cond_host_port = [] # map() takes only one argument + callback, so need to condense hosts + port into one argument
    for port in ports:
        cond_host_port.append((host, port))
    return processor.map(scan_attempt, cond_host_port)

def scan_attempt(host_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_port[0], host_port[1]))
        print("[+] TCP port", host_port[1], "open")
        success = True
    except:
        print("[-] TCP port", host_port[1], "closed")
        success = False
    finally:
        s.close()
    if success:
        return host_port[1]
    else:
        return "Closed"

def get_host_ports():
    print("This is a multi-processing portscanner, which will search through the first 1000 possible TCP ports.")
    host = str(input("Please enter a domain name or IP address: "))
    ports = [x for x in range(1000)]
    return host, ports

def main():
    host, ports = get_host_ports()
    ip = socket.gethostbyname(host)
    print("IP of host:", ip)
    try:
        results = scan(ip, ports)
    except:
        print("Error. Input not satisfactory")
    print("~~~~~~~~")
    print("Results:")
    port_open = False
    for port in results:
        if port != "Closed":
            print("[+] TCP port", port, "open")
            port_open = True
    if port_open == False:
        print("No TCP ports are open on", ip)

if __name__ == "__main__":
    main()
