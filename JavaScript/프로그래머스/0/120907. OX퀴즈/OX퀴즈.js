function solution(quiz) {
    let result = [];

    // 수식 배열을 하나씩 처리
    for (let q of quiz) {
        // 수식을 공백 기준으로 분리
        const parts = q.split(' ');

        // 각 부분을 변수에 할당
        const X = parseInt(parts[0]);
        const operator = parts[1];
        const Y = parseInt(parts[2]);
        const Z = parseInt(parts[4]);

        // 연산자에 맞춰 계산 후 비교
        if (operator === '+') {
            if (X + Y === Z) {
                result.push('O');
            } else {
                result.push('X');
            }
        } else if (operator === '-') {
            if (X - Y === Z) {
                result.push('O');
            } else {
                result.push('X');
            }
        }
    }

    return result;
}
