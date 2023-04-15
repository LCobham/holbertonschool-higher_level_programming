#!/usr/bin/node
// Execute a function X times

exports.addMeMaybe = function (x, theFunction) {
  if (Number(x)) {
    x = Number(x) + 1;
    theFunction(x);
  }
};
