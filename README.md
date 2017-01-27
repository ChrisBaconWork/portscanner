# Portscanner
A multiprocessing TCP port scanner.

This script will take a domain name or IP address as input and run through the first 1000 TCP ports, testing the connection to assess whether each port is open. It will then return the list of open ports.

## How To Use
Download and then cd into the directory and run:

`./portscanner <host> <ports>`

Both `<host>` and `<ports>` are optional. Replace `<host>` with the hostname, and `<ports>` with the maximum number of ports you want to target. If you do not enter a port range, then it will default to 1000 (i.e. TCP ports 0-1000); if you do not enter a hostname, then it will prompt for one during runtime.

## Benchmarking
Why multiprocessing? On my machine, running through the first 1000 TCP ports of my website produces the following results:

Singleprocessing | Multiprocessing
--- | ---
216.20s | 35.01s

There is, then, a considerable improvement in speed if we use the multiprocessing library to do this.

I would like to test the speed of threads as well.
