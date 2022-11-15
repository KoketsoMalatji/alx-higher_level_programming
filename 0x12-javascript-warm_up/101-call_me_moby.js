#!/usr/bin/node

// function that executes x times a function.

exports.callMeMoby = function (x, theFunction) {
  for (let ct = 0; ct < x; ct++) {
    theFunction();
  }
};
