#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  var newList = [];
  for (let i = len - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
