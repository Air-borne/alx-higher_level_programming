#!/usr/bin/node

const list = require('./100-data').list;

const factored = list.map((element, index) => {
  return element * index;
});

console.log(list);
console.log(factored);
