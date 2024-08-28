function solution(my_string, num1, num2) {
    const splits = my_string.split("");
    const core = [...splits[num1]];
    
    splits[num1] = splits[num2];
    splits[num2] = core;
    
    return splits.join("");
}