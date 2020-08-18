#!/bin/bash/
# Get the http status code
curl -Is "$1" -o /dev/null -w '%{http_code}'
