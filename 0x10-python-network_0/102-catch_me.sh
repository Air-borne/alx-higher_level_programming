#!/bin/bash
# send a GET HttpMethod to a server with a respond "You got me!!"
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
