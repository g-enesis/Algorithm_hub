function solution(n) {
    var answer = 0;
    const sqrt = Math.sqrt(n);
    if (Number.isInteger(sqrt)) {
        return 1; // 제곱수라면 1을 반환
    } else {
        return 2; // 제곱수가 아니라면 2를 반환
    }
     
}