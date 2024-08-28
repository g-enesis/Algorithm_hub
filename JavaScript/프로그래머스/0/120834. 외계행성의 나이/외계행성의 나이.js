function solution(age) {
    var answer = '';
    const parse = {
                    "0": "a",
                    "1": "b",
                    "2": "c",
                    "3": "d",
                    "4": "e",
                    "5": "f",
                    "6": "g",
                    "7": "h",
                    "8": "i",
                    "9": "j"
                  }; 
    [...String(age)].map((a, i) => {
      answer += parse[a];
    })
    return answer;
}