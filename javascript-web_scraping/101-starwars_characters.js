#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

const getMovie = new Promise((resolve, reject) => {
  request(url + movieId, (err, response, body) => {
    if (err) {
      reject(err);
    } else {
      const actorURLs = JSON.parse(body).characters;
      resolve(actorURLs);
    }
  });
});

getMovie.then((actorURLs) => {
  const actorPromises = actorURLs.map(actorURL => {
    return new Promise((resolve, reject) => {
      request(actorURL, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          const actorName = JSON.parse(body).name;
          const actorId = actorURL.split('/')[-2];
          resolve([actorName, actorId]);
        }
      });
    });
  });

  Promise.all(actorPromises)
    .then(actorData => {
      actorData.sort((a, b) => a[1] - b[1]);
      actorData.forEach(actor => console.log(actor[0]));
    })
    .catch(err => console.error(err));
});
