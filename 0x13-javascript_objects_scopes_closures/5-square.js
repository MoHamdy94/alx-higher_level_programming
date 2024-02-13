#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call Rectangle's constructor with the same size for both width and height
    super(size, size);
  }
}
module.exports = Square;
