#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const [url, filename] = process.argv.slice(2, 4);

if (url && filename) {
  request(url, (err, response, body) => {
    if (err) {
      console.log('Error occured in the request.');
    } else {
      fs.writeFile(filename, body, 'utf-8', (writeError) => {
        if (writeError) {
          console.log('Error occured when writing file.');
        }
      });
    }
  });
}
