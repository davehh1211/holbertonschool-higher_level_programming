#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$2" | grep Allow | awk '{print $2, $3, $4}'
