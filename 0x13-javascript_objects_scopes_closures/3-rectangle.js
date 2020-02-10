#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && Number.isInteger(h)) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        this.print = function () {
          let msg = '';
          let i = w;
          let j = h;
          while (i) {
            msg += 'X';
            i -= 1;
          }
          while (j) {
            console.log(msg);
            j -= 1;
          }
        };
      }
    }
  }
};
