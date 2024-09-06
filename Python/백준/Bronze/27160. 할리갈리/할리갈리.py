
N = int(input())

# 과일 딕셔너리 선언
dict = {
    "STRAWBERRY": 0, 
    "BANANA": 0, 
    "LIME": 0, 
    "PLUM": 0
}

# 상태값 선언
status = "NO"

for i in range(N):
    # 문자열 입력받기
    F, C = input().split()
    # 과일을 문자열, 개수는 정수로 변환
    fruit, count = str(F), int(C)

    # 선언한 딕셔너리에 각 과일의 갯수를 추가한다.
    dict[fruit] += count
    
    if dict["BANANA"] == 5:
        status = "YES"

    elif dict["LIME"] == 5:
        status = "YES"

    elif dict["PLUM"] == 5:
        status = "YES"

    elif dict["STRAWBERRY"] == 5:
        status = "YES"

    else:
        status = "NO"
    

print(status)
            