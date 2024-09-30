function solution(array) {
  var answer = 0;
  // 각 숫자를 문자열로 변환 후, 문자 단위로 분리
  const splits = [...array].map(a => {
    return String(a).split("");
  });
    
  // 2차원 배열을 1차원 배열을 변환
  const counters = splits.flat();
    
  for (let num of counters) {
    num === "7" ? (answer += 1) : answer;
  }
  return answer;
}