#!/bin/bash

port="8010"


# Start http server. Daemon starts only when port 8000 not busy
busybox httpd -p $port -h .  >> serve.log 2>&1

# Get PID/program of the currently running program at port 
pp=$(netstat -tulnp 2>/dev/null | grep ":$port" | awk '{print $NF}')

# Inform
echo "Port $port is served by $pp"

# Start browser
# This does not leave any traces 
python -m webbrowser -n "http://localhost:$port" > /dev/null 2>&1

