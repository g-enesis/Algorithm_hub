
# 목초지에 있는 풀 덩어리의 수 세기

# 입력
# 지도
# R - 5열
# C - # or .로 이루어진 6행의 문자

# 출력
# 풀 덩어리 수

# 해결 과정
# 초기화: 목초지의 크기 R과 C를 입력받고, 목초지 지도를 .과 #로 이루어진 2차원 배열로 저장합니다.
# 방문 배열: 목초지의 각 위치를 방문했는지 여부를 추적하기 위해 방문 배열(visited)을 사용합니다.
# DFS 또는 BFS 탐색: 각 #를 발견할 때마다 DFS로 해당 덩어리의 모든 인접한 #들을 탐색합니다. 탐색이 끝날 때마다 풀 덩어리의 개수를 1씩 증가시킵니다.
# 결과 출력: 모든 탐색이 끝나면 풀 덩어리의 개수를 출력합니다.
from collections import deque


# 목초지 탐색 문제 해결을 위한 BFS 함수
def bfs(field, visited, start_x, start_y, R, C):
    # 이동할 수 있는 4방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 큐에 시작 위치를 추가하고 방문 처리
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    # 큐가 빌 때까지 BFS 진행
    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 인접한 칸들을 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:  # 목초지 범위 내에 있어야 함
                if not visited[nx][ny] and field[nx][ny] == '#':
                    # 아직 방문하지 않은 인접한 풀 덩어리라면 큐에 추가하고 방문 처리
                    queue.append((nx, ny))
                    visited[nx][ny] = True

# 입력 처리
# R = 5, C = 6
R, C = map(int, input().split())

# ['.#....', '..#...', '..#..#', '...##.', '.#....']
field = [input().strip() for _ in range(R)]

# 방문 여부를 저장할 배열
visited = [[False] * C for _ in range(R)]

# 풀 덩어리 개수를 저장할 변수
lump_count = 0

# 목초지의 모든 위치를 순회
for i in range(R):
    for j in range(C):
        # 현재 위치에 풀이 있고, 아직 방문하지 않았다면 새로운 덩어리로 간주
        if field[i][j] == '#' and not visited[i][j]:
            # BFS를 통해 인접한 모든 풀 덩어리를 방문 처리
            bfs(field, visited, i, j, R, C)
            # 새로운 덩어리를 발견했으므로 개수를 증가
            lump_count += 1

# 결과 출력
print(lump_count)
