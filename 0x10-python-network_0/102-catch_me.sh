#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me and the server respond You got me!, in body
curl -sLX PUT -H "origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
