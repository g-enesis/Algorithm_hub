function solution(s1, s2) {
   
    var answer = s1.filter((item, i) => {
        return s2.includes(item)
    })
    return answer.length;
}