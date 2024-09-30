function solution(n) {
  let factorial = 1;
  let i = 0;
  while (factorial <= n) {
    i++;
    factorial *= i;
  }
  return i - 1;
}

console.log(solution(3628800));
