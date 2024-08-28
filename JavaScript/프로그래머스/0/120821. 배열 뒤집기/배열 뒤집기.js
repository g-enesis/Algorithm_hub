function solution(num_list) {
    var answer = [...num_list];
    let reAnswer = [];
    
    while(answer.length > 0){
       const num = answer.pop();
        reAnswer.push(num)
    } 
    return reAnswer;
}