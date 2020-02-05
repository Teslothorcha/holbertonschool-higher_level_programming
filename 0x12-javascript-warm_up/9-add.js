#!/usr/bin/node
if (parseInt(process.argv.slice(2)[0])) {
  if (parseInt(process.argv.slice(2)[1])) {
    const i = parseInt(process.argv.slice(2)[0]);
    const j = parseInt(process.argv.slice(2)[1]);
    console.log('%i', i + j);
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
