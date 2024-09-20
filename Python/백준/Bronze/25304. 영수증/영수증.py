
# 총 금액
X = int(input())

# 구매한 물건의 종류의 수
N = int(input())

total = X

for i in range(N):
    # a: 물건의 가격, b: 개수
    A, B = map(int, input().split())

    total = total - (A * B)

if total == 0:
    print("Yes")
else:
    print("No")