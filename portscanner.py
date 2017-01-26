#!/usr/bin/env python3
import socket
from multiprocessing import Pool
import click
import sys
import time

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

def get_host_ports(restart):
    print("This is a multi-processing portscanner, which will search through the first 1000 possible TCP ports.")
    if len(sys.argv) > 2 and restart == False:
        host = sys.argv[1]
        portrange = (x for x in range(int(sys.argv[2])))
    elif len(sys.argv) > 1:
        host = sys.argv[1]
        portrange = (x for x in range(1000))
    else:
        host = str(input("Please enter a domain name or IP address: "))
        portrange = (x for x in range(1000))
    return host, portrange  # return host and port generator

def main(restart = False):
    host, ports = get_host_ports(restart)
    try:
        ip = socket.gethostbyname(host)
        print("IP of host:", ip)
    except:
        click.secho("Error. Cannot resolve hostname!", fg="red")
        main(True)
    socket.setdefaulttimeout(0.5)
    results = scan(ip, ports)
    print("~~~~~~~~\nResults:")
    open_ports = (x for x in filter(lambda x: x != "Closed", results)) # open_ports is a generator, meaning the list of open_ports is lazily evaluated
    if open_ports:
        for port in open_ports:
           print("[+] TCP port", port, "open")
    else:
        print("No TCP ports are open on", ip)


if __name__ == "__main__":
    main()
