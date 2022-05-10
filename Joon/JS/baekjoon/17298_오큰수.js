const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const n = +input[0];
const stack = [];

// [3,5,2,7]
const numbers = input[1].split(" ").map(Number);

// [-1,-1,-1,-1]
let result = new Array(n).fill(-1);

for (let i = 0; i < n; i++) {
  while (stack.length && numbers[stack[stack.length - 1]] < numbers[i]) {
    result[stack.pop()] = numbers[i];
  }
  stack.push(i);
}

console.log(result.join(" "));
