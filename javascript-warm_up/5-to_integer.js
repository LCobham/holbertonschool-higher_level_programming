#!/usr/bin/node
/* This module prints to stdout */

const n = Number(process.argv[2]);
if (n) {
  console.log(`My number: ${Math.floor(n)}`);
} else {
  console.log('Not a number');
}
