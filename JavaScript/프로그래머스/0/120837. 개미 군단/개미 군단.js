function solution(hp) {
    var answer = 0;
    
    const ant1 = 5;
    const ant2 = 3;
    const ant3 = 1;
    
    const left1 = hp % ant1;
    const left2 = left1 % ant2;
    const left3 = left2 % ant3;
    
    const left1Result = (hp / ant1);
    const left2Result = (left2 / ant2);
    const left3Result = (left3 / ant3);
    
    if(left3 === 0) {
     answer = left1Result + left2Result + left3Result;
    }
     
    return Math.ceil(answer);
}