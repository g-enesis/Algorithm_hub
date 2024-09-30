const input = require("fs").readFileSync("/dev/stdin").toString();
// const input = require("fs").readFileSync("example.txt").toString();
N = Number(input);

for (let i = 1; i <= N; i++) {
  console.log(i);
}
