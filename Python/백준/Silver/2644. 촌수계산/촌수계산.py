from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited[start] = 0  # 시작 노드 방문, 촌수 0으로 설정
    
    while queue:
        current = queue.popleft()

        if current == end:  # 목적지 도착 시 촌수 반환
            return visited[current]
        
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 아직 방문하지 않은 사람
                visited[neighbor] = visited[current] + 1  # 촌수 증가
                queue.append(neighbor)
    
    return -1  # 목적지에 도달할 수 없는 경우

# 입력 받기
n = int(input())  # 전체 사람 수
start, end = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식 간의 관계 개수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 배열 (-1로 초기화)
visited = [-1] * (n + 1)

# BFS 탐색을 통해 촌수 계산
result = bfs(start, end)

# 결과 출력
print(result)
