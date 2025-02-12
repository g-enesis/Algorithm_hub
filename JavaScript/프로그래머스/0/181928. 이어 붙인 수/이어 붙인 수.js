function solution(num_list) {
    let copy = [...num_list]
    const a = copy.filter((n) => n % 2 === 0 && n);
    const b = copy.filter((n) => n % 2 === 1 && n);
    
    const aSum = a.join("")
    const bSum = b.join("")
    
    return Number(aSum) + Number(bSum) 
}