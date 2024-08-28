function solution(array, height) {
    const newArray = [];
    const filters = array.filter((item) => {
        if(item > height) {
            newArray.push(item)
        }
    })
    return newArray.length;
}