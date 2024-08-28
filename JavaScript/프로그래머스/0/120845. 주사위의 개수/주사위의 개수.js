function solution(box, n) { 
    const case1 = Math.floor(box[0] / n);
    const case2 = Math.floor(box[1] / n);
    const case3 = Math.floor(box[2] / n);
    
    
    return case1 * case2 * case3;
}