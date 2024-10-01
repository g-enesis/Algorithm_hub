function solution(numbers, k) {
  let term = 1;
  for (let i = 1; i < k; i++) {
    term += 2;
    if (term > numbers.length) {
      term -= numbers.length;
    }
  }
  return numbers[term - 1];
}
