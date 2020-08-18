#!/bin/bash/
# Get the http status code
curl -Isw "%{http_code}" "$1" -o /dev/null
