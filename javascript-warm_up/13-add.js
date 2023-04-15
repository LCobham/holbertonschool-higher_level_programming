#!/usr/bin/node
/* This module prints to stdout */

exports.add = function (a, b) {
  if (Number(a) && Number(b)) {
    return (Number(a) + Number(b));
  } else {
    return (NaN);
  }
};
