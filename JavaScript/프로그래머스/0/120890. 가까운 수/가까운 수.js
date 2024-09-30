function solution(array, n) {
  const nears = [...array].map(number => {
    // 1. 배열안의 값에서 n만큼 빼기
    // 2. Math.abs 음수를 양수로 변환
    return { key: number, value: Math.abs(number - n) };
  });

  // 반환된 배열의 최솟값 찾기
  const mini = Math.min(...nears.map(n => n.value));
  return nears
    .filter(near => near.value === mini)
    .map(near => near.key)
    .sort((a, b) => a - b)[0];
}
