function solution(n, numlist) { 
    const filtered = numlist.filter((item) => item % n === 0)
    return filtered;
}