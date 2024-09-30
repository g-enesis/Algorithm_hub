function solution(n) {
  var answer = [];
  // 12, 17, 420 
  for (let i = 2; i <= n; i++) {
    // 나누었을때 0 되야 
    while (n % i === 0) { // while
        // 넣어주고
        answer.push(i);
        // 12 / 2,3,4,5,6,7...12     
        n = n / i;
    }
  }
    // 중복제거
  return [...new Set(answer)];
}

console.log(solution(420));
