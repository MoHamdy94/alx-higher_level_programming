#!/usr/bin/node
const request = require('request');

// Get the URL from the first command-line argument
const url = process.argv[2];

// Send the GET request using request
request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
