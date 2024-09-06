
import sys

# 테스트 케이스 입력받기
T = int(input())

for _ in range(T):
    # sys로 입력을 받아 split한 값들을 정수로 변환하여 a,b 각각 저장.
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
