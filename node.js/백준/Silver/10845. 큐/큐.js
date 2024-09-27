const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
let N = +input.shift();

let queue = [];
let result = [];

for (let i = 0; i < N; i++) {
  const item = input[i];
  const command = item.split(" ")[0];
  const number = item.split(" ")[1];

  switch (command) {
    case "push":
      queue.push(number);
      break;

    case "pop":
      if (queue.length === 0) {
        result.push(-1);
      } else {
        result.push(queue.shift());
      }
      break;

    case "size":
      result.push(queue.length);
      break;

    case "empty":
      if (queue.length === 0) {
        result.push(1);
      } else {
        result.push(0);
      }
      break;

    case "front":
      if (queue.length === 0) {
        result.push(-1);
      } else {
        result.push(queue[0]);
      }
      break;

    case "back":
      if (queue.length === 0) {
        result.push(-1);
      } else {
        result.push(queue[queue.length - 1]);
      }
      break;

    default:
  }
}

console.log(result.join("\n"));
