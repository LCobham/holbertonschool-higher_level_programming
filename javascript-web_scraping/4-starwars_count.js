#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const actorURL = 'https://swapi-api.hbtn.io/api/people/18/';

if (url) {
  request(url, (err, response, body) => {
    if (err) console.log(err);
    else {
      const movies = JSON.parse(body).results;
      let counter = 0;
      for (const movie of movies) {
        if (movie.characters.includes(actorURL)) counter++;
      }
      console.log(counter);
    }
  });
}
