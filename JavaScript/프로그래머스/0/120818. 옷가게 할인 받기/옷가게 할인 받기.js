function solution(price) {
    const percent5 = price * 0.05;
    const percent10 = price * 0.1;
    const percent20 = price * 0.2;
    
    if(100000 > price) {
        return Math.floor(price);
    }
    if(300000 > price) {
        return Math.floor(price - percent5);
    }
    if(500000 > price) {
        return Math.floor(price - percent10);
    }
    if(500000 <= price) {
        return Math.floor(price - percent20);
    } 
}