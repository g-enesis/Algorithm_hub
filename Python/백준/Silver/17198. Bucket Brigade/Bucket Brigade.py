from collections import deque

# 상, 하, 좌, 우 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid, start, end):
    # 시작점 설정
    queue = deque([start])
    visited = [[False] * 10 for _ in range(10)]
    visited[start[0]][start[1]] = True
    distance = [[0] * 10 for _ in range(10)]

    while queue:
        x, y = queue.popleft()

        # 농장(B)에 도달한 경우 경로의 길이 반환
        if (x, y) == end:
            return distance[x][y] - 1  # 소를 놓을 빈 칸의 수는 거리 - 1

        # 인접한 네 방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 그리드 범위 안에 있고, 방문하지 않은 빈 칸이거나 목적지인 경우
            if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny]:
                if grid[nx][ny] == '.' or (nx, ny) == end:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return -1  # 경로가 없는 경우

# 입력 처리
grid = [list(input().strip()) for _ in range(10)]

# 호수(L)와 농장(B)의 좌표 찾기
lake, barn = None, None
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'L':
            lake = (i, j)
        elif grid[i][j] == 'B':
            barn = (i, j)

# BFS로 최단 거리 찾기
result = bfs(grid, lake, barn)
print(result)
