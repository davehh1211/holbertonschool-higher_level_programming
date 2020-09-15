#!/usr/bin/node
let test = process.argv[2];
if (isNaN(test)) {
	console.log('Not a number')
} else {
	console.log('My number is: ' + test)
}
