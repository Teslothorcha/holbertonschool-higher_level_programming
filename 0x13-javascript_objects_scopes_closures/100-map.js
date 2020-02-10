#!/usr/bin/node
const list = require('./100-data').list;
let itera = -1;
const map1 = list.map(fuckit);
function fuckit (num) {
  itera += 1;
  return num * itera;
}
console.log(list);
console.log(map1);
