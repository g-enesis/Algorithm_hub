
import heapq
import sys

input = sys.stdin.read

# 입력 받기
data = input().splitlines()

# 연산의 개수 N
N = int(data[0])

min_heap = []
result = []

# N값으로 인해 1부터 시작
for i in range(1, N+1):
    x = int(data[i])

    # x가 자연수인지 확인
    if x > 0:
        # 자연수라면 힙 추가
        heapq.heappush(min_heap, x)

    # x가 0이라면
    elif x == 0:
        # 배열에 정수가 들어있는지 비어있는지 
        if min_heap: 
            # 우선순위 제거(최소값)
            result.append(heapq.heappop(min_heap))
        # 배열이 비어있다면 0 저장
        else:
            result.append(0)
# print()
# print(result)

for res in result:
    print(res)