#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let row = 0; row < w; row++) {
      let line = '';
      for (let col = 0; col < w; col++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}
module.exports = Rectangle;
