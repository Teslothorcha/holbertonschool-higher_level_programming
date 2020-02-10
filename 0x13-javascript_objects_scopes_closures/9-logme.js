#!/usr/bin/node
let times = 0;
exports.logMe = function (item) {
  console.log('%i: %s', times, item);
  times += 1;
};
