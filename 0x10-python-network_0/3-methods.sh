#!/bin/bash
# specify all http methods that the server accepts
curl -iLX OPTIONS "$1" |grep -w "Allow" | cut -f2 -d":"
