#!/usr/bin/node
/* This module prints to stdout */

function factorial(a) {
  if (a && a > 0 && Math.floor(a) === a) {
    if (a === 1) {
      return (1);
    }
    return (a * factorial(a - 1));
  }
  return (1);
}

console.log(factorial(Number(process.argv[2])));
