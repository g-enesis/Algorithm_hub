function solution(s) {
  const frequency = {};

  for (let char of s) {
    frequency[char] = (frequency[char] || 0) + 1;
  }
  // console.log(Object.keys(frequency));
  const uniqueChars = Object.keys(frequency).filter(
    char => frequency[char] === 1,
  );
  // console.log(uniqueChars);
  return uniqueChars.length > 0 ? uniqueChars.sort().join("") : [];
}

// console.log(solution("hello"));
