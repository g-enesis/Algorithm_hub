function solution(balls, share) {
  const count = combinations(balls, share);
  console.log(count);
  return count;
}

function combinations(n, k) {
  // k가 n보다 크면 조합은 불가능하므로 0 반환
  if (k > n) return 0;

  // k가 n/2보다 크면 C(n, k) = C(n, n-k) 를 사용하여 계산
  if (k > n - k) {
    k = n - k;
  }

  // 조합 수 계산
  let numerator = 1;
  let denominator = 1;

  for (let i = 0; i < k; i++) {
    numerator *= n - i;
    denominator *= i + 1;
  }

  return numerator / denominator;
}

// // 예제 호출
// console.log(solution(3, 2)); // 3
// console.log(solution(5, 3)); // 10
// console.log(solution(5, 5)); // 1
// console.log(solution(5, 6)); // 0
