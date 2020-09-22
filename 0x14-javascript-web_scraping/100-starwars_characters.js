#!/usr/bin/node
const request = require('request');
const movie = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(movie, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonfile = JSON.parse(body).characters;
    for (const characters in jsonfile) {
      request(jsonfile[characters], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const jsonchar = JSON.parse(body);
          console.log(jsonchar.name);
        }
      });
    }
  }
}
);
