function solution(name, yearning, photo) {
    const yearningMap = new Map();

    name.forEach((n, i) => {
        yearningMap.set(n, yearning[i]);
    });

    return photo.map(group => 
        group.reduce((sum, person) => sum + (yearningMap.get(person) || 0), 0)
    );
}
