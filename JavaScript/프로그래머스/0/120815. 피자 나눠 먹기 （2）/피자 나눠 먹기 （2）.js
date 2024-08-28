function solution(n) { 
    let result = 0;
    let pizza = 6;
    let count = pizza % n;
    
    for(let i=1; i<=100; i++){
        if(pizza % n === 0){
            result = i;
            break;
        }else {
            pizza = pizza + 6;
            continue;
        }
    }
    
    return result;
}