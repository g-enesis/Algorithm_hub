function solution(my_string, n) {
    let answer = "";
    let spl = my_string.split("");
    
    for(let i=0; i<spl.length; i++){
        for(let j=0; j<n; j++){
            answer += spl[i]
        }
    }
    
    return answer;
}