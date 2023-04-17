#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

if (movieId) {
  request(url + movieId, (err, response, body) => {
    if (err) console.log(err);
    else {
      const characters = JSON.parse(body).characters;
      for (const actorURL of characters) {
        request(actorURL, (actorError, actorResponse, actorBody) => {
          if (actorError) console.log(actorError);
          else {
            console.log(JSON.parse(actorBody).name);
          }
        });
      }
    }
  });
}
