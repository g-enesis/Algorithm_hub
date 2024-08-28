function solution(n, k) {
    let yang = 12000;
    let drink = 2000;
    
    let sum = (yang * n) + (drink * k);
    
    const tips = Math.floor(n / 10);
    
    return sum - drink * tips;
}