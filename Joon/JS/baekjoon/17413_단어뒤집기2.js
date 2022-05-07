// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

const input = "baekjoon online judge\n";

let stackRight = [];
let stackReverse = [];
let result = "";
let toggle = false;

for (x of input) {
  if (x === "<") {
    toggle = true;
    while (stackReverse.length) {
      result += stackReverse.pop();
    }
  }
  if (toggle) {
    stackRight.push(x);
  } else {
    if (x === " ") {
      while (stackReverse.length) {
        result += stackReverse.pop();
      }
      result += " ";
    } else {
      stackReverse.push(x);
    }
  }
  if (x === ">") {
    toggle = false;
    result += stackRight.join("");
    stackRight = [];
  }
}

while (stackReverse.length) {
  result += stackReverse.pop();
}

console.log(result);
