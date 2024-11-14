function solution(polynomial) {
    // 각 항을 구분해서 배열로 나누기
    const terms = polynomial.split(' + ');
    let xCoefficient = 0;
    let constant = 0;

    terms.forEach(term => {
        if (term.includes('x')) {
            // 'x'만 있을 때는 계수를 1로 처리
            const coefficient = term === 'x' ? 1 : parseInt(term);
            xCoefficient += coefficient;
        } else {
            // 상수항
            constant += parseInt(term);
        }
    });

    // 결과 문자열을 구성
    let result = [];
    if (xCoefficient > 0) {
        result.push(xCoefficient === 1 ? 'x' : `${xCoefficient}x`);
    }
    if (constant > 0) {
        result.push(constant.toString());
    }

    return result.join(' + ');
}
