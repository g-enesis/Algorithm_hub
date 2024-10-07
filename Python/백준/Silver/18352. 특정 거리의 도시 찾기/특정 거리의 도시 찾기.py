import sys
from collections import deque

input = sys.stdin.read

def find_cities_at_distance_k(N, M, K, X, roads):
    # 1. 그래프 초기화 (인접 리스트)
    graph = [[] for _ in range(N + 1)]
    for A, B in roads:
        graph[A].append(B)
    
    # 2. 각 도시에 대한 최단 거리 테이블 초기화
    distance = [-1] * (N + 1)  # 모든 도시에 대해 -1로 초기화
    distance[X] = 0  # 출발 도시 X의 거리는 0
    
    # 3. BFS 탐색
    queue = deque([X])
    
    while queue:
        current_city = queue.popleft()
        
        # 현재 도시에서 연결된 모든 도시를 확인
        for next_city in graph[current_city]:
            if distance[next_city] == -1:  # 아직 방문하지 않은 도시만 탐색
                distance[next_city] = distance[current_city] + 1
                queue.append(next_city)
    
    # 4. 결과 출력 (최단 거리가 K인 도시 찾기)
    result = [city for city in range(1, N + 1) if distance[city] == K]
    
    if result:
        return result
    else:
        return [-1]

# 입력 처리
data = input().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])
X = int(data[3])

roads = []
index = 4
for _ in range(M):
    A = int(data[index])
    B = int(data[index + 1])
    roads.append((A, B))
    index += 2

# 결과 출력
result = find_cities_at_distance_k(N, M, K, X, roads)
sys.stdout.write('\n'.join(map(str, result)) + '\n')
