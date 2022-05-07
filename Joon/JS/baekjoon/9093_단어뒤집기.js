const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const t = Number(input[0]);

function reverse(string) {
  let stack = [];
  let answer = "";
  for (let i = 0; i < string.length; i++) {
    stack.push(string[i]);
  }

  for (let i = 0; i < string.length; i++) {
    answer += stack.pop();
  }

  return answer;
}

let result = [];
for (let i = 1; i < input.length; i++) {
  result.push(input[i].split(" ").map(reverse));
}

for (let i = 0; i < result.length; i++) {
  console.log(result[i].join(" "));
}
