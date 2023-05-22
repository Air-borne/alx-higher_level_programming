#!/usr/bin/node

const str = 'C is fun';
const argv = process.argv;

const x = parseInt(argv[2]);
if (Number.isInteger(x) === false) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
