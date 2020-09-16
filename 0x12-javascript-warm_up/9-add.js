#!/usr/bin/node
const numb1 = process.argv[2];
const numb2 = process.argv[3];
function add (a, b) {
  return Number(a) + Number(b);
}
console.log(add(numb1, numb2));
