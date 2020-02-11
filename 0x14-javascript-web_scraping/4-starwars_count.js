#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error.toString());
  } else {
    let cuenta = 0;
    const results = JSON.parse(body).results;
    results.forEach(peli => {
      const per = peli.characters;
      per.forEach(es => {
        if (es.includes('/18/')) {
          cuenta += 1;
        }
      }
      );
    }
    );
    console.log(cuenta);
  }
});
