function solution(dot) {
     
    const dots = [...dot]; // [2,4]
    
    const dot0 = Math.sign(dot[0]);
    const dot1 = Math.sign(dot[1]);
    
    // 둘 다 양수
    if(dot0 === 1 && dot1 === 1){
        return 1
    }
    // y가 음수
    else if(dot0 === 1 && dot1 === -1){
        return 4
    }
    // x가 음수
    else if(dot0 === -1 && dot1 === 1){
        return 2
    }
    // x, y 둘 다 음수
    else if(dot0 === -1 && dot1 === -1) {
      return 3  
    } 
      
}