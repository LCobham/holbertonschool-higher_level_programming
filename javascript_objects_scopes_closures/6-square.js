#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (myChar = 'X') {
    if (this.height && this.width) {
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          process.stdout.write(myChar);
        }
        console.log();
      }
    }
  }
}

module.exports = Square;
