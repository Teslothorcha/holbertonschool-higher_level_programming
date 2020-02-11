#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const fs = require('fs');
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error.toString());
  }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      return (console.log(err));
    }
  });
});
