#!/usr/bin/node
let myNumber = process.argv[2];
if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  while (myNumber) {
    console.log('C is fun');
    myNumber--;
  }
}
