#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) === true &&
    Number.isInteger(h) === true) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = [];
    for (let j = 0; j < this.width; j++) {
      line += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(line);
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
