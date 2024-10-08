import sys
from collections import Counter

# 입력 받기
N = int(input())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

# 1. 산술평균
mean = round(sum(numbers) / N)

# 2. 중앙값
numbers.sort()
median = numbers[N // 2]

# 3. 최빈값
count = Counter(numbers)
modes = count.most_common()
# 최빈값 중 여러 개 있을 때 두 번째로 작은 값을 찾기 위한 처리
max_freq = modes[0][1]
mode_candidates = [m[0] for m in modes if m[1] == max_freq]
mode_candidates.sort()

if len(mode_candidates) > 1:
    mode = mode_candidates[1]  # 최빈값이 여러 개면 두 번째로 작은 값
else:
    mode = mode_candidates[0]  # 최빈값이 하나면 그 값을 출력

# 4. 범위
range_value = max(numbers) - min(numbers)

# 출력
print(mean)        # 산술평균
print(median)      # 중앙값
print(mode)        # 최빈값
print(range_value) # 범위
