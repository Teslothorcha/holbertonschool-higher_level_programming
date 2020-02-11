#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error.toString());
  }
  let cuenta = 0;
  const results = JSON.parse(body).results;
  for (let i = 0; i < JSON.parse(body).count; i++) {
    if (results[i].characters.includes('https://swapi.co/api/people/18/')) {
      cuenta += 1;
    }
  }
  console.log(cuenta);
});
