function solution(numbers) {
    const sortNumbers = [...numbers].sort((a, b) => a - b);
    return Math.max(
        sortNumbers[0] * sortNumbers[1], 
        sortNumbers[sortNumbers.length - 1] * sortNumbers[sortNumbers.length - 2]
    )
}