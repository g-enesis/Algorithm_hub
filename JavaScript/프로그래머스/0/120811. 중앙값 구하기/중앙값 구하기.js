function solution(array) {
    var answer = 0;
    const orders = [...array].sort((a, b) => b - a);
    const lengths = Math.floor(orders.length / 2);
    
    return orders[lengths];
}