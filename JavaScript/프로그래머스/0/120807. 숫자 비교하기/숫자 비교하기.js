function solution(num1, num2) {
    return isVars(num1) && isVars(num2) ? cals(num1, num2) : null;
}
const isVars = (vars) => 0 <= vars <= 10000;
const cals = (num1, num2) => {
   return num1 === num2 ? 1 : -1;
    
}