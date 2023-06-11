#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const noop = () => {};

if (argv.length > 4) {
  fs.readFile(argv[2], undefined, function (err, data) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(argv[4], data, { flag: 'w+' }, noop);
  });
  fs.readFile(argv[3], undefined, function (err, data) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(argv[4], data, { flag: 'a' }, noop);
  });
}
