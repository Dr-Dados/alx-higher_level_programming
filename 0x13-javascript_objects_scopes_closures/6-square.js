#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      console.log((!c ? 'X' : 'C').repeat(this.width));
    }
  }
}

module.exports = Square;
