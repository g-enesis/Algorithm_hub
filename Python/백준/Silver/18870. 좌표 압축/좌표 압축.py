# 좌표 압축의 구현
# - 주어진 A[1], A[2], ..., A[n]를 좌표 압축시키기
#   1. A[1], A[2], ..., A[n]를 정렬한 새로운 배열 B[]를 만듦
#   2. 필요 시 중복된 원소들을 제거
#   3. 각 A[i]를 B[]에서 이분탐색하여 인덱스를 계산

# 총 시간복잡도는 O(n log n)

import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# print(A)
# [2, 4, -10, 4, -9]

B = sorted(list(set(A)))
# print(B)
# [-10, -9, 2, 4]

dic = {}

for i in range(len(B)):
    key, value = B[i], i
    dic[key] = value

# print(dic)
# {-10: 0, -9: 1, 2: 2, 4: 3}

for i in A:
    print(dic[i], end = ' ')
# 2 3 0 3 1