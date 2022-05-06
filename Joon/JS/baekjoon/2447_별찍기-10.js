"use strict";
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);

let str = "";

function printStar(i, j) {
  if (i % 3 === 1 && j % 3 === 1) {
    str += " ";
  } else {
    if (Math.floor(i / 3) === 1 && Math.floor(j / 3) === 1) {
      str += " ";
    } else {
      str += "*";
    }
  }
}

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    printStar(i, j);
  }
  str += "\n";
}

console.log(str);
