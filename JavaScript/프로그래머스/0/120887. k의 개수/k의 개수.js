function solution(i, j, k) {
    let answer = 0;
    const stringK = String(k);
    
    for(let a=i; a<=j; a++){
        const stringA = String(a);
        // stringA 에 k가 포함되어있다면
         if(stringA.includes(stringK)){
            let cnt = 0;
             // stringA 인자에서 k를 찾는다.
             for(let c of stringA) {
                 if(c === stringK){
                 // 찾을 때마다 +1
                   answer++;
                 }
             }
            
         }
         
        
    }
    return answer;
}