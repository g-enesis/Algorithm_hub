function solution(age) { 
    return isVars(age) ? calcAge(age) + 1 : null;
}
const isVars = (vars) => 0 < vars <= 120;
const calcAge = (age) => {
    const year = 2022;
    return year - age;
}