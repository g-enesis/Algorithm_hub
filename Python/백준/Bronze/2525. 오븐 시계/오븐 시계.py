import math

# 입력 받기
h, m = map(int, input().split())
t = int(input())

# 분과 시간을 계산
m += t
h += m // 60
m %= 60
h %= 24

print(h, m)
