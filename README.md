# Portscanner
A multiprocessing TCP port scanner

This script will take a domain name or IP address as input and run through the first 1000 TCP ports, testing the connection to assess whether each port is open. It will then return the list of open ports.

## How To Use
Easy enough. Download the script and run it. But this is mostly an exercise for myself so I haven't bothered to create a setup file or anything like that.

Either enter the host on the command line, after the script name, or as an input once the program has started. The second cli argument is also optional and will indicate the number of ports to scan. The default is 1000 (i.e. TCP port 0 to 1000):

`./portscanner <url> <ports>`

Both `<url>` and `<ports` are optional.
