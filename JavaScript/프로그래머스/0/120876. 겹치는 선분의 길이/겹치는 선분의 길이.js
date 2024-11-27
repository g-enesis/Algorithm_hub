function solution(lines) {
    // 범위를 관리하기 위해 선분의 모든 점을 포함할 수 있는 배열을 생성
    const lineMap = new Array(201).fill(0); // -100부터 100까지 포함하려면 길이가 201이어야 함

    // 선분의 시작과 끝 좌표를 배열에 반영
    for (const [start, end] of lines) {
        for (let i = start + 100; i < end + 100; i++) {
            lineMap[i] += 1;
        }
    }

    // 겹치는 부분의 길이를 계산 (2개 이상의 선분이 겹친 경우)
    return lineMap.filter(count => count > 1).length;
}
