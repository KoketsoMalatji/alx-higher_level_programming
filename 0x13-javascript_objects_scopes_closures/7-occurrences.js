#!/usr/bin/node

// Returns the number of occurrences of an element in a list

exports.nbOccurences = function (list, searchElement) {
  let iter = 0;
  const sizeof = list.length;
  for (let ct = 0; ct < sizeof; ct++) {
    if (searchElement === list[ct]) {
      iter++;
    }
  }
  return iter;
};
