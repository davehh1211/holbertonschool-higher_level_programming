#!/usr/bin/node
let maxNum = 0;
const arg = process.argv.slice(2);
if (arg.length > 1) {
  arg.sort((a,b)=>a-b);
  console.log(arg)
  maxNum = arg[arg.length - 2];
}
console.log(Number(maxNum));
