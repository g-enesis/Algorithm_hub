const [x, y, w, h] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ");

const d1 = x - 0;
const d2 = w - x;
const d3 = h - y;
const d4 = y - 0;

const stateMin = Math.min(d1, d2, d3, d4);

console.log(stateMin);
