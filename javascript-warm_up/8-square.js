#!/usr/bin/node
/* This module prints to stdout */

const n = Number(process.argv[2]);
if (n && n > 0) {
  const floor = Math.floor(n);
  for (let i = 0; i < floor; i++) {
    let res = '';
    for (let j = 0; j < floor; j++) {
      res += 'X';
    }
    console.log(res);
  }
} else if (!n) {
  console.log('Missing size');
}
