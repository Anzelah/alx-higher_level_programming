#!/bin/bash
# specify all http methods that the server accepts
curl -sI ALLOW "$1" -L |grep -w "Allow" | cut -f2 -d":"
