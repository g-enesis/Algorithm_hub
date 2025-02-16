function solution(t, p) {
    let count = 0;
    const len = p.length;

    // `t`에서 길이가 `len`인 부분 문자열들을 순차적으로 확인
    for (let i = 0; i <= t.length - len; i++) {
        const substring = t.slice(i, i + len);
        if (Number(substring) <= Number(p)) {
            count++;
        }
    }

    return count;
}
