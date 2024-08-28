function solution(numbers, direction) {
    var answer = [...numbers];
    
    switch(direction) {
        case "right":
            const r = answer.pop();
            answer.unshift(r);
            return answer;
            
        case "left":
           const l = answer.shift();
            answer.push(l);
            return answer;
    }
}