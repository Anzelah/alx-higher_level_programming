#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length === 2 || arr.length === 3) {
    return 0;
  }

  let largest = arr[2];
  let secondLarge = arr[3];

  for (let i = 2; i < arr.length; i++) {
    if (arr[i] > largest) {
      secondLarge = largest;
      largest = arr[i];
    } else if (arr[i] > secondLarge && arr[i] < largest) {
      secondLarge = arr[i];
    }
  }
  return (secondLarge);
}

const ans = secondBiggest(process.argv);
console.log(ans);
