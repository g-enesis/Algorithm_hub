function solution(numbers) {
    var answer = [];
    const newNumbers = numbers.map((number)=> {
        return number * 2
    })
    return newNumbers;
}