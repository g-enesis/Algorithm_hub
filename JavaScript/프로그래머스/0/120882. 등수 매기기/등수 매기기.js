function solution(score) {
    const averages = score.map(s => (s[0] + s[1]) / 2);
    const sortedAverages = [...averages].sort((a, b) => b - a); 
    const ranks = averages.map(avg => sortedAverages.indexOf(avg) + 1);
    
    return ranks;
}