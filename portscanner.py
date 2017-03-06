#!/usr/bin/env python3
import socket, click, sys, time, threading, argparse
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
        click.secho("[+] TCP port" + " " + str(host_port[1]) + " " + "open", fg="green")
        s.close
        return host_port[1]
    except:
        print("[-] TCP port", str(host_port[1]), "closed")
        s.close
        return "Closed"

def get_host_ports(restart):
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", dest="domain", required=True, help="host/domain to run scan against")
        parser.add_argument("-p", dest="ports", help="number of ports to scan")
        args = parser.parse_args()

        if args.ports:
            host, portrange = args.domain, (x for x in range(int(args.ports)))
        else:
            host, portrange = args.domain, (x for x in range(1000))
        return host, portrange

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
