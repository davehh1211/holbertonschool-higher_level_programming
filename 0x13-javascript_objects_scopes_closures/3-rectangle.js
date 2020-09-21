#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let t = 0; t < this.height; t++) {
      console.log('X'.repeat(this.width));
    }
  }
};
