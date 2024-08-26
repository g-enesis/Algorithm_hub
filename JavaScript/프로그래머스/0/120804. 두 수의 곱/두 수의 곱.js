function solution(num1, num2) {
    return isVars(num1) && isVars(num2) ? num1 * num2 : null;
}

const isVars = (vars) => 0 <= vars <= 100;