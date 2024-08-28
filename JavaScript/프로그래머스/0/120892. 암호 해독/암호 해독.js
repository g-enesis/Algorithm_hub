function solution(cipher, code) {
    let result = "";
    var answer = cipher.split("").join("");
     for(let i=1; i<=answer.length; i++) {
        result += answer[code * i-1] ? answer[code * i-1] : ""
     }
        
    
    return result;
}