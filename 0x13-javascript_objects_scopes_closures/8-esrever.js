#!/usr/bin/node

// function that returns the reversed version of a list

exports.esrever = function (list) {
  const listReversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listReversed.push(list[i]);
  }
  return listReversed;
};
