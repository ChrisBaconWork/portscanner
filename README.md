# Portscanner
A multiprocessing TCP port scanner

This script will take a domain name or IP address as input and run through the first 1000 TCP ports, testing the connection to assess whether each port is open. It will then return the list of open ports.

## How To Use
Easy enough. Download the script and run it. But this is mostly an exercise for myself so I haven't bothered to create a setup file or anything like that.

Either enter the host on the command line, after the script name, or as an input once the program has started.

## TODO
* Invalid input handler only works for user input (i.e. not when the host is a cli argument)
