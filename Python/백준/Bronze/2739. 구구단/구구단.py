
# N 입력 받아서 정수로 변환
N = int(input())

# 1단부터 9단(start: 1, end: 10, step: 1)을 전개
for i in range(1, 10, 1):
    # f-string(파이썬 3.6이상)으로 표현
    print(f"{N} * {i} = {N * i}")