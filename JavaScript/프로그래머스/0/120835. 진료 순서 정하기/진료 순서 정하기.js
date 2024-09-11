 
function solution(emergency) {
    // 배열의 각 원소와 그 원소의 인덱스를 쌍으로 묶어서 저장
    const indexedEmergency = emergency.map((value, index) => {
        return { value, index };
      /*
        [{ value: 3, index: 0 }, { value: 76, index: 1 }, { value: 24, in dex: 2 }] 
      */
    });
    
    // 응급도에 따라 내림차순으로 정렬                              
    indexedEmergency.sort((a,b) => b.value - a.value);
    // [{ value: 76, index: 1 }, { value: 24, index: 2 }, { value: 3, index: 0 }]
    
    // 원래 인덱스 순서로 정렬된 배열 생성
    const result = new Array(emergency.length); // [undefined, undefined, undefined]
    
    
    indexedEmergency.forEach((item, rank) => {
        result[item.index] = rank + 1;
    })
                                     
                                
    return result
}
