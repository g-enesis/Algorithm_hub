function solution(my_str, n) {
  const answer = [];
  let s = 0;

  // 반복 횟수 계산 (전체 문자열 길이를 n으로 나누어 올림)
  const forIdx = Math.ceil(my_str.length / n);
  
  for (let i = 0; i < forIdx; i++) {
    // 문자열을 n 길이로 잘라서 answer 배열에 추가
    let slicedStr = my_str.slice(s, s + n);
    answer.push(slicedStr);
    s += n; // 시작 인덱스를 n만큼 증가시킴
  }

  return answer;
}

