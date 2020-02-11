#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (err, data) => {
  if (data === undefined) {
    console.log(err);
  } else {
    process.stdout.write(data.toString());
  }
});
