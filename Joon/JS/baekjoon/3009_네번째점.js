"use strict";

const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const X = {};
const Y = {};

inputs.forEach((input) => {
  let [x, y] = input.split(" ");
  X[x] = X[x] + 1 || 0;
  Y[y] = Y[y] + 1 || 0;
});

console.log(
  Object.keys(X).find((key) => X[key] === 0),
  Object.keys(Y).find((key) => Y[key] === 0)
);
