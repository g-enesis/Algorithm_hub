function solution(num_list, n) {
    let result = [];
    
    // num_list를 n개의 원소를 가진 하위 배열로 나누기
    for (let i = 0; i < num_list.length; i += n) {
        result.push(num_list.slice(i, i + n));
    }
    
    return result;
}