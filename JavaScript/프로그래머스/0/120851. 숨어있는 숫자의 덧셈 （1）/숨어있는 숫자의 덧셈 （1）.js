function solution(my_string) {
    var answer = 0;
    my_string.replace(/[a-zA-Z]/g, "").split("").map((str)=> {
        answer += Number(str)
    })
    return answer;
}