
import math

# N바이트 정수
N = int(input())

longs = ""

if N % 4 == 0:
    for i in range(math.floor(N/4)+1):
        longs = "long " * i + "int"

print(longs)
