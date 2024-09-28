# 테스트 케이스 수 입력
t = int(input())

for _ in range(t):
    # 의상 수 입력
    n = int(input())
    
    # 의상 종류별로 의상을 저장할 딕셔너리
    clothes = {}
    
    # 의상 입력
    for _ in range(n):
        name, kind = input().split()
        
        # 의상 종류별로 의상 수 카운트
        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1
    
    # 경우의 수 계산
    result = 1
    for count in clothes.values():
        result *= (count + 1)
    
    # 알몸이 아닌 경우를 출력하기 위해 -1
    print(result - 1)
