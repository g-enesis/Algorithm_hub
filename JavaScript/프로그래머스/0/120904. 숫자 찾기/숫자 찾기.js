function solution(num, k) {
    var answer = [...String(num)];
   
    if(answer.indexOf(String(k)) === -1) {
        return -1;
        
    } else {
       return answer.indexOf(String(k)) + 1;
    }
    
    
}