class CircleQueue {
  constructor(maxSize) {
    this.maxSize = maxSize;
    this.queue = [];
    this.front = 0;
    this.rear = 0;
    this.size = 0;
  }

  enqueue(value) {
    if (this.isFull()) return console.log("꽉 찼습니다.");
    this.queue[this.rear] = value;
    this.rear = (this.rear + 1) % this.maxSize;
    this.size++;
  }

  dequeue() {
    if (this.isEmpty()) return console.log("이미 비어있습니다.");
    const value = this.queue[this.front];
    delete this.queue[this.front];
    this.front = (this.front + 1) % this.maxSize;
    this.size--;
    return value;
  }

  isFull() {
    return this.size === this.maxSize;
  }

  isEmpty() {
    return this.size === 0;
  }
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, K] = input[0].split(" ").map((num) => +num);
const queue = new CircleQueue(N);
let result = [];

for (let i = 1; i <= N; i++) {
  queue.enqueue(i);
}

let count = 0;
while (!queue.isEmpty()) {
  count++;
  if (count % K === 0) {
    result.push(queue.dequeue());
  } else {
    queue.enqueue(queue.dequeue());
  }
}

console.log(`<${result.join(", ")}>`);
