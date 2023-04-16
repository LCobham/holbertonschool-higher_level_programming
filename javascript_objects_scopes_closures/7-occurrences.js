#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const elmnt of list) {
    if (elmnt === searchElement) n++;
  }
  return (n);
};
