function solution(my_string) {
  var answer = my_string.split(" ");
  let value = parseInt(answer[0]);

  // console.log("fist value: ", value);
  let numItems = [];
  let calcItems = [];

  answer.map(item => {
    if (item !== "+" && item !== "-") numItems.push(item);
    if (item === "+" || item === "-") calcItems.push(item);
  });

  // console.log("numItems: ", numItems);
  // console.log("calcItems:", calcItems);

  calcItems.map((item, i) => {
    // console.log(item);
    if (item === "+") {
      value += parseInt(numItems[i + 1]);
      // console.log(value);
    }
    if (item === "-") {
      value -= parseInt(numItems[i + 1]);
      // console.log(value);
    }
  });
  // console.log("last value: ", value);
  return value;
}
solution("3 + 4 - 1 + 1");
