function solution(bin1, bin2) {
  let carry = 0;
  let answer = "";

  let maxLength = Math.max(bin1.length, bin2.length);

  // 두 이진수의 길이를 맞추기 위해 앞에 0을 채움
  bin1 = bin1.padStart(maxLength, "0");
  bin2 = bin2.padStart(maxLength, "0");

  // 뒤에서부터 하나씩 더해줌
  for (let i = maxLength - 1; i >= 0; i--) {
    const sum = parseInt(bin1[i]) + parseInt(bin2[i]) + carry;
    if (sum >= 2) {
      carry = 1; // 2 이상이면 자리 올림이 필요
      answer = (sum % 2) + answer; // 0 또는 1을 추가
    } else {
      carry = 0;
      answer = sum + answer;
    }
  }

  // 마지막으로 carry가 남아있으면 앞에 1을 추가
  if (carry === 1) {
    answer = "1" + answer;
  }

  return answer;
}

console.log(solution("10", "11")); // "101"
console.log(solution("1001", "1111")); // "11000"
