function solution(s, skip, index) {
    // 사용 가능한 알파벳 리스트 만들기
    const alphabet = [...'abcdefghijklmnopqrstuvwxyz'].filter(c => !skip.includes(c));

    // 변환된 문자열 만들기
    return [...s].map(char => {
        let newIndex = (alphabet.indexOf(char) + index) % alphabet.length;
        return alphabet[newIndex];
    }).join('');
}