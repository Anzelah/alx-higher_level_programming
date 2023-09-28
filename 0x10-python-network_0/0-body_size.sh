#!/bin/bash
# Display size of body
curl -sI "$1" | grep -w "Content-Length" | cut -f2 -d " "
