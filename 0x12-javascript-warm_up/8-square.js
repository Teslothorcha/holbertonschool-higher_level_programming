#!/usr/bin/node
let msg = '';
if (parseInt(process.argv.slice(2)[0])) {
  if (parseInt(process.argv.slice(2)[0]) >= 1) {
    let i = parseInt(process.argv.slice(2)[0]);
    let j = i;
    while (i) {
      msg += 'X';
      i -= 1;
    }
    while (j) {
      console.log(msg);
      j -= 1;
    }
  }
} else {
  console.log('Missing size');
}
