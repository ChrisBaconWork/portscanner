# Portscanner
A multiprocessing TCP port scanner

This script will take a domain name or IP address as input and run through the first 1000 TCP ports, testing the connection to assess whether each port is open. It will then return the list of open ports.

## How To Use
Easy enough. Download the script and run it. But this is mostly an exercise for myself so I haven't bothered to create a setup file or anything like that.

cd into the directory and run:

`./portscanner <host> <ports>`

Both `<host>` and `<ports>` are optional. Replace `<host>` with the hostname, and `<ports>` with the maximum number of ports you want to target. If you do not enter a portrange, then it will default to 1000 (i.e. TCP ports 0-1000).
