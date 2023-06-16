#!/bin/bash
#display the options that are allowed on the URL
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
