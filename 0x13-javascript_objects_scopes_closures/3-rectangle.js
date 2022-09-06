#!/usr/bin/node
// Rectangle class
class Rectangle {
  constructor (width, height) {
    if ((width = parseInt(width)) > 0 &&
        (height = parseInt(height)) > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
