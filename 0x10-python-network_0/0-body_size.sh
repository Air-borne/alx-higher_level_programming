#!/bin/bash
# a bash script that returns the length of the content
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
