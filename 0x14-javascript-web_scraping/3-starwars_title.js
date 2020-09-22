#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const movieId = process.argv[2];
request.get(`https://swapi-api.hbtn.io/api/films/${movieId}}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
