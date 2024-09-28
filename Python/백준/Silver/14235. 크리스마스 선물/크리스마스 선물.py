import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄에서 아이들과 거점지를 방문한 횟수 n을 입력 받는다.
n = int(data[0])

# 최대 힙을 사용하기 위해 heapq를 사용하되, 음수 값을 이용하여 처리
max_heap = []
result = []

for i in range(1, n + 1):
    line = list(map(int, data[i].split()))
    a = line[0]
    
    if a > 0:
        # 거점지에서 a개의 선물을 충전하는 경우
        for gift in line[1:]:
            # 최대 힙을 위해 음수로 저장
            heapq.heappush(max_heap, -gift)
    else:
        # 아이들을 만났을 때
        if max_heap:
            # 가장 가치가 큰 선물을 준다 (음수를 다시 양수로 변환)
            result.append(-heapq.heappop(max_heap))
        else:
            # 줄 선물이 없다면 -1 출력
            result.append(-1)

# 결과 출력
for res in result:
    print(res)
