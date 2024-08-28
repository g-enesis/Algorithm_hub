function solution(sides) {
    const sorts = [...sides].sort((a, b) => b - a);
    const angle = { x: sorts[0], y: sorts[1], z: sorts[2] };
 
    return (angle.y + angle.z) > angle.x ? 1 : 2; 
    
}