#!/usr/bin/node
/* This module prints to stdout */

const n = Number(process.argv[2]);
if (n && n > 0) {
  for (let i = 0; i < Math.floor(n); i++) {
    console.log('C is fun');
  }
} else if (!n) {
  console.log('Not a number');
}
