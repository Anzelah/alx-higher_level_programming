#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + ep, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
