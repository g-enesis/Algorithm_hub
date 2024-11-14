function solution(numlist, n) {
    return numlist.sort((a, b) => {
        const distanceA = Math.abs(a - n);
        const distanceB = Math.abs(b - n);
        
        // 거리 기준으로 오름차순 정렬
        if (distanceA !== distanceB) {
            return distanceA - distanceB;
        }
        // 거리가 같을 경우, 더 큰 값을 앞에 배치
        return b - a;
    });
}
