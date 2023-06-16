#!/bin/bash
# Display allowed methods on the given url
curl -sI $1 | grep Allow | cut -c8-
