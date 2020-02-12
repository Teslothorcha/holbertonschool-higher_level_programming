#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url, function (error, response, body) {
  if (error) {
    return console.log(error.toString());
  }
  const todos = JSON.parse(body);
  const dic = {};
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      if (dic[todos[i].userId] === undefined) {
        dic[todos[i].userId] = 1;
      } else {
        dic[todos[i].userId] += 1;
      }
    }
  }
  console.log(dic);
});
