#!/bin/bash
# This program takes in a URL, sends a request to that URL
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
