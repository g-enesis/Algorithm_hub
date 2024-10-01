function solution(sides) {
  let answer = 0;

  // 주어진 두 변 중 최대 값과 최소 값을 구함
  const maxSide = Math.max(...sides);
  const minSide = Math.min(...sides);

  // 1. 가장 긴 변이 maxSide인 경우
  // 나머지 한 변이 minSide + outSide > maxSide 조건을 만족해야 함
  for (let outSide = maxSide - minSide + 1; outSide <= maxSide; outSide++) {
    answer++;
  }

  // 2. 나머지 한 변이 가장 긴 변인 경우
  // maxSide + minSide > outSide 조건을 만족하는 경우
  for (let outSide = maxSide + 1; outSide < minSide + maxSide; outSide++) {
    answer++;
  }

  return answer;
}

// 예제 호출
console.log(solution([1, 2])); // 1
console.log(solution([3, 6])); // 5
console.log(solution([11, 7])); // 13
