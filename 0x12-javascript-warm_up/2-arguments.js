#!/usr/bin/node

let args;
if (process.argv.length === 2) {
  args = 'No argument';
  console.log(args);
} else if (process.argv.length === 3) {
  args = 'Argument found';
  console.log(args);
} else {
  args = 'Arguments found';
  console.log(args);
}
