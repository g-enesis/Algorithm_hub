
def is_multiple_of_three(X):
    # 변환 횟수 카운트
    count = 0
    
    # 주어진 수 X를 계속 변환
    while len(X) > 1:  # 한 자리 수가 아닐 때까지 반복
        count += 1
        # 각 자리수의 합을 구한다
        Y = sum(int(digit) for digit in X)
        X = str(Y)  # 새로운 Y를 문자열로 변환하여 X에 저장
    
    # 최종 Y가 3의 배수인지 확인
    if int(X) in [3, 6, 9]:
        result = "YES"
    else:
        result = "NO"
    
    return count, result

# 입력 받기
X = input().strip()

# 결과 얻기
count, result = is_multiple_of_three(X)

# 출력
print(count)
print(result)