#!/usr/bin/node
// Gets the title of a Star wars film using the Star wars API

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(apiUrl, async (filmErr, filmRes, filmBody) => {
  if (filmErr) {
    console.log(filmErr);
  } else {
    const character = JSON.parse(filmBody).characters;
    for (let i = 0; i < character.length; i++) {
      const result = await new Promise((resolve, reject) => {
        request.get(character[i], (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body);
          }
        });
      });
      console.log(JSON.parse(result).name);
    }
  }
});
