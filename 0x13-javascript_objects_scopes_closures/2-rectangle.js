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
}
module.exports = Rectangle;
