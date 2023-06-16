#!/bin/bash
# This script send a json POST request to the endpoint
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
