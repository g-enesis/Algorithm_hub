import heapq

# 국회의원 후보 수
N = int(input())

# 다솜이 표
dasom = int(input())

# 나머지 국회의원들 표
others = []

# 나머지 국회의원들 표를 힙큐에 저장(-1로 max_heap 적용)
for _ in range(N - 1):
    heapq.heappush(others, -int(input()))

# 뺏어올 사람들 수
take = 0

# 다른 국회의원들보다 다솜이 표가 많을때까지 반복
while others and -others[0] >= dasom:
    # 가장 많은 표를 가진 국회의원의 표(음수 >> 양수 변환)
    max_user = -heapq.heappop(others)

    # 가장 많은 표를 가진 국회의원의 표에서 1표를 뺏어온다.
    max_user -= 1

    # 다솜이에게 1표를 추가
    dasom += 1

    # 뺏어왔으니 뺏어올 사람 수 1표 추가
    take += 1

    # 표수가 남아있다면 힙에 추가
    heapq.heappush(others, -max_user)

print(take)