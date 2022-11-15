#!/bin/bash
# This script takes in a URL and displays all HTTP methods
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
