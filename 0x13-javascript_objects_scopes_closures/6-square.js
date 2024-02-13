#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    // Call Rectangle's constructor with the same size for both width and height
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
}
module.exports = Square;
