function solution(my_string) {
    var answer = [...my_string].map((str) => str.toLowerCase());
    return answer.sort().join("");
}