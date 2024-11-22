function solution(common) {
    // 등차수열 판단: 공차 계산
    if (common[1] - common[0] === common[2] - common[1]) {
        // 등차수열이면 마지막 원소에 공차를 더함
        return common[common.length - 1] + (common[1] - common[0]);
    }
    
    // 등비수열 판단: 공비 계산
    if (common[1] / common[0] === common[2] / common[1]) {
        // 등비수열이면 마지막 원소에 공비를 곱함
        return common[common.length - 1] * (common[1] / common[0]);
    }
}