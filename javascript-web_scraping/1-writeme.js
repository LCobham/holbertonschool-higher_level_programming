#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
let data = process.argv[3];

if (filename) {
  if (!data) {
    data = '';
  }
  fs.writeFile(filename, data, 'utf-8', (err) => {
    if (err) console.error(err);
  });
}
