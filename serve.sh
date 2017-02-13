#!/bin/bash


# Start http server. Daemon starts only when port 8000 not busy
busybox httpd -p 8010 -h .  >> serve.log 2>&1

# Get status. 0 only if daemon started. When port is busy, exit status is 1
s=$?

# Inform
if [ "$s" == "0" ]; then
    echo "New daemon started"
else
    echo "Daemon already exists"
fi    

# Start browser
# This does not leave any traces 
python -m webbrowser -n 'http://localhost:8010' > /dev/null 2>&1

