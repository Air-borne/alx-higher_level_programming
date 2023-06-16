#!/usr/bin/node
//This scipt saves the output to a file

const request = require('request');
const fs = require('fs');

const fileName = process.argv[3];
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error retrieving webpage:', error);
    return;
  }
  
  fs.writeFile(fileName, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return;
    }
    
    console.log( fileName);
  });
});

