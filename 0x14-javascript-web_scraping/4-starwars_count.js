#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonfile = JSON.parse(body).results;
    let count = 0;
    for (const things in jsonfile) {
      const charlist = jsonfile[things].characters;
      for (const each in charlist) {
        if (charlist[each].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
