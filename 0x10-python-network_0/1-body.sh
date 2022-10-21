#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response
# takes in URL and redirects to new location
# prints the body of a response only if status is 200
if [ "$(curl -sL -o /dev/null -sw '%{http_code}' "$1")" -eq 200 ]; then curl -sL "$1"; fi
