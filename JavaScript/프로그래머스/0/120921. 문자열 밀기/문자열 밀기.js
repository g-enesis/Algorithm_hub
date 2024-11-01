function solution(A, B) {
    const n = A.length;
    
    // A를 오른쪽으로 한 칸 밀기 위한 함수
    const shift = (str) => str[n - 1] + str.slice(0, n - 1);
    
    // B와 일치하는 경우 찾기
    for (let i = 0; i < n; i++) {
        if (A === B) {
            // 현재 i 횟수에서 일치하면 반환
            return i;
        }
        // A를 한 칸 밀기
        A = shift(A);
    }
    
    // 일치하지 않으면 -1 반환
    return -1;
}