#!/bin/bash
# specify all http methods that the server accepts
curl -sI "$1" | grep -w "Allow" | cut -f2
