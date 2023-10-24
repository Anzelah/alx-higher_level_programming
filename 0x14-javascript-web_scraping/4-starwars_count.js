#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const id = 18;

request(url, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
	  let count = 0;
	  const all = JS.parse(body).results;
//	  for (let result = 0; result < all.length; result++)
  }
});
