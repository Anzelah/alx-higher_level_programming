#!/bin/bash
# send a request to return a specific message
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
