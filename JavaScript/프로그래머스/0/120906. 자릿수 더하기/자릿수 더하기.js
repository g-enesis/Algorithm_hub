function solution(n) {
    let strings = String(n);
    let spl = strings.split("");
    let numbers = spl.map((str) => Number(str));
    return numbers.reduce((a, b) => a + b)
}