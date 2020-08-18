#!/bin/bash/
# Get the http status code
curl -ILs "$1" -o /dev/null -w '%{http_code}'
