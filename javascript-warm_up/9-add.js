#!/usr/bin/node
/* This module prints to stdout */

function add(a, b) {
  if (Number(a) && Number(b)) {
    console.log(Number(a) + Number(b));
  } else {
    console.log(NaN);
  }
}

add(process.argv[2], process.argv[3])
