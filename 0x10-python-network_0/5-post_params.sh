#!/bin/bash
# Sends a post request to given url
curl -sd 'email=test@gmail.com&subject=I will always be here for PLD' -X POST $1
