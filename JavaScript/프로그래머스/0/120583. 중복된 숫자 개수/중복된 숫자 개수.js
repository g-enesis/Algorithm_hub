function solution(array, n) {
    const newArray = [];
    const filters = array.filter((item)=> {
        if(item === n) newArray.push(item)
    });
    return newArray.length;
}