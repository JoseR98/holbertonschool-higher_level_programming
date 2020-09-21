#!/usr/bin/node
// Class Square that inherits from Rectangle class
module.exports = class Square extends required('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charPrint(c) {
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
