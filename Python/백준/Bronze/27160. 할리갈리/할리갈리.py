
# 카드의 개수 입력받는다.
N = int(input())

# 카드 과일종류와 과일개수를 담을 딕셔너리 선언
fruits = {
    "STRAWBERRY": 0,
    "BANANA": 0,
    "LIME": 0,
    "PLUM": 0,
}

# 결과값 변수
result = "NO"

# 카드개수만큼 반복한다.
for i in range(N):
    # 카드 1장을 뒤집어본다.
    a, b  = input().split()
    # 과일종류와 과일개수를 타입에 맞게 변수에 저장한다.
    type, amount = a, int(b)

    # 딕셔너리에 정의된 과일에 과일개수를 추가해준다.
    fruits[type] += amount

# 딕셔너리 과일중에서 과일의 개수가 정확히 5개가 있다면
if any(value == 5 for value in fruits.values()):
    result = "YES"
else:
    result = "NO"

print(result)