#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument
curl -s "$1" -X DELETE
