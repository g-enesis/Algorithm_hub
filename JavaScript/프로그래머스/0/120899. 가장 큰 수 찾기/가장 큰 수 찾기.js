function solution(array) {
    const item = [...array].sort((a, b)=> b - a)[0];
    var answer = [item, array.indexOf(item)];
    return answer;
}