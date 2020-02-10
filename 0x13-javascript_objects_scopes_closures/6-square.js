#!/usr/bin/node
const Squaree = require('./5-square');
module.exports = class Square extends Squaree {
  charPrint (c = 'X') {
    let msg = '';
    let i = this.width;
    let j = this.height;
    while (i) {
      msg += c;
      i -= 1;
    }
    while (j) {
      console.log(msg);
      j -= 1;
    }
  }
};
