function solution(num_str) {
    var answer = num_str.split("");
    const intArr = answer.map(str => parseInt(str, 10));
    return intArr.reduce((a, b) => a + b);
    
}