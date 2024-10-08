function solution(spell, dic) {
    var answer = 0;
    const dics = [...dic].sort();
    const sortedSpell = [...spell].sort().join("");
    
    for(let word of dic) {
        if(sortedSpell === word.split("").sort().join("")) {
            return 1;
        }
    }
    return 2;
}