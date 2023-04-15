#!/usr/bin/node
/* This module prints to stdout */

if (process.argv.length < 4) {
  console.log(0);
} else {
  let biggest = Number(process.argv[2]);
  let second = -Infinity;
  for (let i = 3; i < process.argv.length; i++) {
    const n = Number(process.argv[i]);
    if (n > biggest) {
      second = biggest;
      biggest = n;
    } else if (n > second) {
      second = n;
    }
  }
  console.log(second);
}
