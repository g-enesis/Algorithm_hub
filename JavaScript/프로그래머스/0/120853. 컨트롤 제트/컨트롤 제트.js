function solution(s) {
  var answer = 0;
  const lists = s.split(" ");

  lists.map((num, i) => {
    if (num === "Z") {
      answer -= lists[i - 1];
    } else {
      answer += parseInt(num);
    }
  });
  return answer;
}
solution("10 Z 20 Z");
