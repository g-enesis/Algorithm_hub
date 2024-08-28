function solution(numbers) { 
    const sortNums = numbers.sort((a,b)=> a-b)
    return sortNums[sortNums.length -1 ] * sortNums[sortNums.length -2 ] 
}