function solution(money) {
    let americano = 5500;
    let count = ~~(money / americano);
    let leftMoney = money % americano;
    var answer = [count, leftMoney];
    return answer;
}