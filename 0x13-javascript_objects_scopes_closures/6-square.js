#!/usr/bin/node
const SquareModel = require('./5-square');

class Square extends SquareModel {
  constructor (size) {
    // Call Rectangle's constructor with the same size for both width and height
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
