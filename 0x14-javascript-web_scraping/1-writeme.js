#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const line = process.argv[3];
fs.writeFile(file, line, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
