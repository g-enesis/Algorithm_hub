function solution(dots) {
    // 두 점을 잇는 직선의 기울기를 계산하는 함수
    const calculateSlope = (dot1, dot2) => {
        const [x1, y1] = dot1;
        const [x2, y2] = dot2;
        return (y2 - y1) / (x2 - x1);
    };

    // 네 점 중 두 점을 선택하는 모든 조합
    const combinations = [
        [0, 1, 2, 3], // [dots[0], dots[1]], [dots[2], dots[3]]
        [0, 2, 1, 3], // [dots[0], dots[2]], [dots[1], dots[3]]
        [0, 3, 1, 2]  // [dots[0], dots[3]], [dots[1], dots[2]]
    ];

    // 조합마다 기울기를 비교하여 평행 여부 확인
    for (const [i1, i2, i3, i4] of combinations) {
        const slope1 = calculateSlope(dots[i1], dots[i2]);
        const slope2 = calculateSlope(dots[i3], dots[i4]);
        if (slope1 === slope2) {
            return 1; // 평행한 직선이 있음
        }
    }

    return 0; // 평행한 직선이 없음
}
