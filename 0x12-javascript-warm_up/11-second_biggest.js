#!/usr/bin/node
const arg = process.argv;
let maxNum = 0;
if (arg.length === 2) {
  console.log(0);
} else if (Number(arg[2]) === 1) {
  console.log(0);
} else {
  maxNum = arg.sort();
  console.log(maxNum[maxNum.length - 2]);
}
