#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let line = [];
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      line += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(line);
    }
  }
};
