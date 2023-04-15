#!/usr/bin/node
// Execute a function X times

exports.callMeMoby = function (x, theFunction) {
  if (Number(x) && x > 0) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
  }
}
