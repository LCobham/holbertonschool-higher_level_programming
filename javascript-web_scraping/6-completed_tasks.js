#!/usr/bin/node

const request = require('request');
const apiURL = process.argv[2];

if (apiURL) {
  request(apiURL, (err, response, body) => {
    if (err) console.log(err);
    else {
      const apiResponse = JSON.parse(body);
      const userTasks = {};
      for (const task of apiResponse) {
        if (task.completed) {
          if (userTasks[task.userId] !== undefined) {
            userTasks[task.userId]++;
          } else {
            userTasks[task.userId] = 1;
          }
        }
      }
      console.log(userTasks);
    }
  });
}
