function solution(babbling) {
    const validSounds = ["aya", "ye", "woo", "ma"];
    let count = 0;

    for (let word of babbling) {
        let isValid = true;

        // 같은 발음이 두 번 연속으로 나오는 경우 확인
        for (let sound of validSounds) {
            if (word.includes(sound.repeat(2))) {
                isValid = false;
                break;
            }
        }

        if (isValid) {
            // 정규 표현식으로 유효한 발음만 반복 없이 제거
            const pattern = /^(aya|ye|woo|ma)+$/;
            if (pattern.test(word)) {
                count++;
            }
        }
    }

    return count;
}
