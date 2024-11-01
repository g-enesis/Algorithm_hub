function solution(chicken) {
    let maxServiceChicken = 0;
    let coupon = chicken;
    
    // 쿠폰이 10장 이상일 때만 서비스 치킨을 주문할 수 있음
    while (coupon >= 10) { 
        const serviceChicken = Math.floor(coupon / 10);
        maxServiceChicken += serviceChicken;
        
        // 서비스 치킨으로 받은 쿠폰 + 남은 쿠폰
        coupon = serviceChicken + (coupon % 10); 
    }
    
    return maxServiceChicken;
}
