function solution(a, b) {
    //기약분수로 만들기 위해 a와 b의 최대공약수를 구한다.
    const gcdValue = gcd(a, b);
    
    //b를 최대공약수로 나누어 기약분수로 만든다.
    b /= gcdValue;
    
    //b의 소인수를 2와 5로 나누기
    while (b % 2 === 0) b /= 2;
    while (b % 5 === 0) b /= 5;
    
    //b가 1이면 유한소수, 아니면 무한소수
    return b === 1 ? 1 : 2;
}

//a와 b의 최대공약수
function gcd(x, y) {
    while (y !== 0) {
        const temp = y;
        y = x % y;
        x = temp;
    }
    return x;
}
