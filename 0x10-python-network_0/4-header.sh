#!/bin/bash
#cURL that sends a GET Request to the URL
curl -sX -H "X-School-User-Id: 98" GET $1 -L
