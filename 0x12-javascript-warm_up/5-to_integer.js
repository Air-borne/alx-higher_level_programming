#!/usr/bin/node

const argv  = process.argv;
const value = parseInt(argv[2]);
if (Number.isInteger(value) === false) {
    console.log ('Not a number');
} else {
    console.log ('My number: ' + value);
}
