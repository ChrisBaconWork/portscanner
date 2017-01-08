#!/usr/bin/env python3
import socket
from multiprocessing import Pool
import click
import sys

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
        click.secho("[+] TCP port" + " " + str(host_port[1]) + " " + "open", fg="green")
        s.close
        return host_port[1]
    except:
        print("[-] TCP port", str(host_port[1]), "closed")
        s.close
        return "Closed"

def get_host_ports():
    print("This is a multi-processing portscanner, which will search through the first 1000 possible TCP ports.")
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = str(input("Please enter a domain name or IP address: "))
    return host, [x for x in range(1000)] # return host and ports

def main():
    host, ports = get_host_ports()
    try:
        ip = socket.gethostbyname(host)
        print("IP of host:", ip)
    except:
        click.secho("Error. Cannot resolve hostname!", fg="red")
        main()
    socket.setdefaulttimeout(0.5)
    results = scan(ip, ports)
    print("~~~~~~~~\nResults:")
    port_open = False
    for port in results:
        if port != "Closed":
            print("[+] TCP port", port, "open")
            port_open = True
    if port_open == False:
        print("No TCP ports are open on", ip)

if __name__ == "__main__":
    main()
