function solution(my_string) {
  var answer = my_string.split(" ");
  let value = parseInt(answer[0]);

  let numItems = [];
  let calcItems = [];

  answer.map(item => {
    if (item !== "+" && item !== "-") numItems.push(item);
    if (item === "+" || item === "-") calcItems.push(item);
  });

  calcItems.map((item, i) => {
    if (item === "+") {
      value += parseInt(numItems[i + 1]);
    }
    if (item === "-") {
      value -= parseInt(numItems[i + 1]);
    }
  });
  return value;
}
solution("3 + 4 - 1 + 1");
