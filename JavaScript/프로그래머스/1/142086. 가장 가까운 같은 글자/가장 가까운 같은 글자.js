function solution(s) {
    const lastIndex = new Map();
    return [...s].map((char, i) => {
        const prevIndex = lastIndex.get(char) ?? -1;
        lastIndex.set(char, i); // 현재 위치 저장
        return prevIndex === -1 ? -1 : i - prevIndex;
    });
}