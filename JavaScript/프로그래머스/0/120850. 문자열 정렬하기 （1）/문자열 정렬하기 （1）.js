function solution(my_string) {
    var answer = my_string;
    //1. my_string의 숫자부분만 필터링한 문자열을 만들자
    //2. 만든 문자열을 split으로 쪼개어 새로운 배열로 만들자
    //3. 만든 배열을 sort로 오름차순 정렬을 하자
    let newStr = answer.replace(/[^0-9]/g, "");
    let splStr = newStr.split("")
    
     return splStr.map((str) => Number(str)).sort((a, b) => (a - b));
}