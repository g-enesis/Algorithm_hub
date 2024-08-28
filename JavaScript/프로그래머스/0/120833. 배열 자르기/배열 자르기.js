function solution(numbers, num1, num2) {
    var answer = [...numbers];
    return answer.slice(num1, num2 + 1);
}