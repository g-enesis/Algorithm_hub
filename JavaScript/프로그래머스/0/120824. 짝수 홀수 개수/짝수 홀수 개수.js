function solution(num_list) {
    let item = { a: 0, b: 0 };
    num_list.map((num) => {
        num % 2 === 0 && item.a++;
        num % 2 !== 0 && item.b++;
    })
    var answer = [item.a, item.b];
    return answer;
}