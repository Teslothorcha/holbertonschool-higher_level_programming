#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h)) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print () {
    let msg = '';
    let i = this.width;
    let j = this.height;
    while (i) {
      msg += 'X';
      i -= 1;
    }
    while (j) {
      console.log(msg);
      j -= 1;
    }
  }

  rotate () {
    const moment = this.height;
    this.height = this.width;
    this.width = moment;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
