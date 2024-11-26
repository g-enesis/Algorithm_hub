function solution(board) {
    const n = board.length; // n x n 배열의 크기
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],          [0, 1],
        [1, -1], [1, 0], [1, 1]
    ];

    // 위험 지역 표시를 위한 복사 배열 생성
    const dangerZone = Array.from({ length: n }, () => Array(n).fill(0));

    // 지뢰 주변을 위험 지역으로 표시
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (board[i][j] === 1) {
                // 현재 위치와 주변 8방향을 위험 지역으로 표시
                dangerZone[i][j] = 1;
                for (const [dx, dy] of directions) {
                    const x = i + dx;
                    const y = j + dy;
                    if (x >= 0 && x < n && y >= 0 && y < n) {
                        dangerZone[x][y] = 1;
                    }
                }
            }
        }
    }

    // 안전 지역 계산
    let safeCount = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (dangerZone[i][j] === 0) {
                safeCount++;
            }
        }
    }

    return safeCount;
}
