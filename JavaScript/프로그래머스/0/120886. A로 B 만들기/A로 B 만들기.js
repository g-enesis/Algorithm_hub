function solution(before, after) {
  let sortedBefore = [...before].sort().join();
  let sortedAfter = [...after].sort().join();
  // console.log(sortedBefore);
  // console.log(sortedAfter);

  if (sortedBefore === sortedAfter) {
    return 1;
  } else {
    return 0;
  }
}

console.log(solution("olleh", "hello")); // 1
console.log(solution("allpe", "apple")); // 0
