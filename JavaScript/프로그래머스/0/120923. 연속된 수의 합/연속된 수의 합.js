function solution(num, total) {
    // 연속된 수의 첫 번째 값 계산
    const start = Math.floor((total - (num * (num - 1)) / 2) / num);
    // 연속된 수 배열 생성
    return Array.from({ length: num }, (_, i) => start + i);
}
