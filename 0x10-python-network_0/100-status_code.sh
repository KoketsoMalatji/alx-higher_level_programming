#!/bin/bash
# Script that sends a request and displays only status code
curl -s "$1" -o /dev/null -w "%{http_code}"
