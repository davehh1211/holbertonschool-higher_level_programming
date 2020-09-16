#!/usr/bin/node
const myNumb = process.argv[2];
function factorial (myNumb) {
  if (isNaN(myNumb) || myNumb === 1) {
    return (1);
  } else {
    return (myNumb * factorial(myNumb - 1));
  }
}
console.log(factorial(Number(myNumb)));
