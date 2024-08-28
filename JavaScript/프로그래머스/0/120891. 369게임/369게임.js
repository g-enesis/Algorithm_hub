function solution(order) {
    var answer = [...String(order)].filter((item)=>{
       return item === "3" || item === "6" | item === "9" && item
    });
    
    return answer.length;
}