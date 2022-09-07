#!/usr/bin/node

// prints My number: <first argument converted in integer>

const myVar = process.argv[2];

if (myVar === undefined || isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(myVar));
}
