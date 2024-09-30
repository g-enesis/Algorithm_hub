function solution(my_string) {
  if (my_string.match(/\d+/g)) {
    
    var answer = my_string.match(/\d+/g).map(Number);
    return answer.reduce((a, b) => a + b, 0);
  } else {
    return 0
  }
}
