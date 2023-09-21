#!/usr/bin/node

function factorial (n) {
  if (isNaN(parseInt(n))) {
    return 1;
  }
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const number = process.argv[2];
const ans = factorial(number);
console.log(ans);
