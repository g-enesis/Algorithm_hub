# N의 길이를 가지는 A, B
# A는 = 재정렬 가능
# B를 = 재정렬 불가능
# S의 최솟값 구하기

# A를 오름차순 정렬
# B에서 가장 큰 수와 A에서 가장 작은 수를 곱한 값을 S에 더하기
# max(B)에서 pop하기
# B에서 가장 큰 수와 A에서 N번째로 큰 수를 곱한 값을 S에 더하기

N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
S = 0

# print("A: ", A)
# A: [1 1 1 6 0]

# print("B: ", B)
# B: [2 7 8 3 1]

for i in range(N):
    # B에서 가장 큰 값을 가져온다.
    max_B = max(B)
    # print("max_B: ", max_B)

    # A[0], A[1], A[2] ... x B에서 가장 큰 값
    S += A[i] * max_B
    # print("S: ", S)

    # 0 x 8 = 0
    # 1 x 7 = 7
    # 1 x 3 = 3
    # 1 x 2 = 2
    # 6 x 1 = 6
    # total = 18

    # B에서 가장 큰 8 제거
    # B에서 가장 큰 7 제거
    # B에서 가장 큰 3 제거
    # B에서 가장 큰 2 제거
    # B에서 가장 큰 1 제거
    B.remove(max_B)

    # B
    # [2, 7, 3, 1]
    # [2, 3, 1]
    # [2, 1]
    # [1]
    # []

    # print(B)
    


print(S)