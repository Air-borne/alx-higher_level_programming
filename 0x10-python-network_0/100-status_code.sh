#!/bin/bash
# write to stdout the status of the request
curl -o /dev/null -sw "%{http_code}" $1
