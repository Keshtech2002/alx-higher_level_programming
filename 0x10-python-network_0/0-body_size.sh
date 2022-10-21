#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# display number of bytes in location
curl -sI $1 | grep -oP 'Content-Length: \K\d+'
