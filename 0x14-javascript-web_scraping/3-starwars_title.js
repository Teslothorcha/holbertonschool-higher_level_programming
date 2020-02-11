#!/usr/bin/node
const url = 'http://swapi.co/api/films/' + process.argv[2];
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error.toString());
  }
  console.log(JSON.parse(body).title);
});
