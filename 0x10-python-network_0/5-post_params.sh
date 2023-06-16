#!/bin/bash
#Using POST and setting parameters
curl -sX POST "email=test@gmail.com&subject=I will always be here for PLD" $1 -L
