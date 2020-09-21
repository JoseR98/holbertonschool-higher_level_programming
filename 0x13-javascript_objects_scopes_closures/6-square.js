#!/usr/bin/node
// Class Square that inherits from Rectangle class
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint(c=undefined) {
    for (let hei = 0; hei < this.height; hei++) {
      let result = '';
      for (let wid = 0; wid < this.width; wid++) {
        if (c) {
          result += 'C';
        } else {
          result += 'X';
        }
      }
      console.log(result);
    }
  }
};
