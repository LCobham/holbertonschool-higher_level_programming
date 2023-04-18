#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = Number(process.argv[2]);

if (Number.isInteger(id)) {
  request(url + id, (err, response, body) => {
    if (err) console.log(err);
    else {
      console.log(JSON.parse(body).title);
    }
  });
}
