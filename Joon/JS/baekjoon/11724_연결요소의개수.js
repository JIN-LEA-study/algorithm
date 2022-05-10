"use strict";

class Queue {
  constructor() {
    this.queue = [];
    this.front = 0;
    this.rear = 0;
  }

  enqueue(value) {
    this.queue[this.rear++] = value;
  }

  dequeue() {
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front++;
    return value;
  }

  isEmpty() {
    return this.rear === this.front;
  }
}
const fs = require("fs");
const input = fs.readFileSync("input.txt").toString().trim().split("\n");
// const input = "6 5\n1 2\n2 5\n5 1\n3 4\n4 6\n".split("\n");

const [n, m] = input[0].split(" ").map(Number);

const graph = Array.from(new Array(n + 1), () => []);
const visited = new Array(n + 1).fill(0);
for (let i = 1; i <= m; i++) {
  const [src, dest] = input[i].split(" ").map(Number);
  graph[src].push(dest);
  graph[dest].push(src);
}

console.log(graph);

const queue = new Queue();
let count = 0;

for (let i = 1; i <= n; i++) {
  if (visited[i] === 0) {
    count += 1;
    queue.enqueue(i);
    while (!queue.isEmpty()) {
      const src = queue.dequeue();
      for (const dest of graph[src]) {
        if (visited[dest] === 0) {
          queue.enqueue(dest);
          visited[dest] = 1;
        }
      }
    }
  }
}

console.log(count);
