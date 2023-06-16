#!/bin/bash
#Prints size of body of the response when sending http request to url
curl -s $1 | wc -c
