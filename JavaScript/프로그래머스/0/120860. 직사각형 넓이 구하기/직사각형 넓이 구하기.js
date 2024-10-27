function solution(dots) {
    var answer = 0;
    const sortedDots = dots.sort((a, b) => a[0] - b[0])
    const calY = Math.abs(sortedDots[0][1] - sortedDots[1][1]);
    const calX = Math.abs(sortedDots[0][0] - sortedDots[2][0])
    return calX * calY;
}