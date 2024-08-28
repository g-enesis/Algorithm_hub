function solution(my_string) {
    var answer = '';
    const strArray = my_string.split("").map((item)=> {
        if(item === item.toUpperCase()){
            return answer += item.toLowerCase();
        } else if(item === item.toLowerCase()) {
            return answer += item.toUpperCase();
        } else {
            return;
        }
    })    
    return answer;
}