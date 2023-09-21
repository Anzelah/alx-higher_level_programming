#!/usr/bin/node

const text = 'C is fun';

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
}

let i = 0;
const times = process.argv[2];
while (i < times) {
  console.log(text);
  i++;
}
