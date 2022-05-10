"use strict";

// const input = require("fs")
//   .readFileSync("input.txt")
//   .toString()
//   .trim()
//   .split("\n");

const input = "dmih\n11\nB\nB\nP x\nL\nB\nB\nB\nP y\nD\nD\nP z\n".split("\n");

const string = input[0];
const n = +input[1];

const leftStack = [];
const rightStack = [];

for (let x of string) {
  leftStack.push(x);
}

for (let i = 2; i < input.length; i++) {
  const command = input[i].split(" ");
  switch (command[0]) {
    case "P":
      leftStack.push(command[1]);
      break;
    case "L":
      if (leftStack.length) rightStack.push(leftStack.pop());
      break;
    case "D":
      if (rightStack.length) leftStack.push(rightStack.pop());
      break;
    case "B":
      if (leftStack.length) leftStack.pop();
      break;
  }
}

while (rightStack.length) {
  leftStack.push(rightStack.pop());
}
console.log(leftStack.join(""));
