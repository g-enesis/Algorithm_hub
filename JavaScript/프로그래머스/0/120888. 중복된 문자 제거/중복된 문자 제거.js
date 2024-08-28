function solution(my_string) {
    let result = '';
    for (let i = 0; i < my_string.length; i++) {
        if(i === my_string.indexOf(my_string[i])) {
            result += my_string[i];
        }
    }
    return result;
}