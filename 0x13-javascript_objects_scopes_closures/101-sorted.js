#!/usr/bin/node

const dict = require('./101-data').dict;

const result = {};
for (const [key, value] of Object.entries(dict)) {
  if (result[value] === undefined) {
    result[value] = [];
  }
  result[value].push(key);
}

console.log(result);
