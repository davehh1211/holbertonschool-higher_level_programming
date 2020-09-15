#!/usr/bin/node
const myVar = process.argv.slice(2);
if (myVar[0]) {
  console.log(myVar[0]);
} else if (myVar) {
  console.log('No argument');
}
