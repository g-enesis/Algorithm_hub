function solution(n, t) {
    let total = n;
    for(let i=1; i<=t; i++) {
        total = total * 2;
    }
    return total;
}