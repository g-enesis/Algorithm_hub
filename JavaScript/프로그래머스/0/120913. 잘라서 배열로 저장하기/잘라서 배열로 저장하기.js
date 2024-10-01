function solution(my_str, n) {
  const answer = [];
  let s = 0;

  // 필요한 반복 횟수 계산 (소수점 올림)
  const forIdx = Math.ceil(my_str.length / n);

  for (let i = 0; i < forIdx; i++) {
    let slicedStr = my_str.slice(s, s + n); // s에서 시작하여 n만큼 슬라이스
    answer.push(slicedStr);
    s += n; // 시작 인덱스를 n만큼 증가시킴
  }

  return answer;
}
