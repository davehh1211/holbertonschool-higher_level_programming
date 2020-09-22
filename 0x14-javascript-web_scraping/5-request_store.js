#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile('loripsum', body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
