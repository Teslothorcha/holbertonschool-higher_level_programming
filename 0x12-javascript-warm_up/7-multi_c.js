#!/usr/bin/node
if (parseInt(process.argv.slice(2)[0])) {
  const myVar = 'C is fun';
  let i = parseInt(process.argv.slice(2)[0]);
  while (i) {
    console.log(myVar);
    i -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}
