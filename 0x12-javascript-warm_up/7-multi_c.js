#!/usr/bin/node
let myNumber = process.argv[2];
if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  while (myNumber > 0) {
    console.log('C is fun');
    myNumber--;
  }
}
