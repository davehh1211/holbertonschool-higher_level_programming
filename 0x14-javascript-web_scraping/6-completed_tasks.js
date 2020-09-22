#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const newDict = {};
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonfile = JSON.parse(body);
    for (const m of jsonfile) {
      if (m.completed === true) {
        if (newDict[m.userId]) {
          newDict[m.userId]++;
        } else {
          newDict[m.userId] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
