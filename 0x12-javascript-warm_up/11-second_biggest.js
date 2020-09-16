#!/usr/bin/node
const arg = process.argv.slice(2);
let maxNum = 0;
if (arg.length > 1) {
  arg.sort();
  maxNum = arg[arg.length - 2];
}
console.log(Number(maxNum));
