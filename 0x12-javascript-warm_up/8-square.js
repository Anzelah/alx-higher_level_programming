#!/usr/bin/node

const times = process.argv[2];

if (isNaN(parseInt(times))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    let str = '';
    for (let j = 0; j < times; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
