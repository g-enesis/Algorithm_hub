# 양의 수 > 늑대의 수 = 양이 다 잡아먹는다.
# 그 외엔 늑대가 다 잡아먹는다.

# 빈 공간  : "."
# 울타리   : "#"
# 늑대    : "v"
# 양     : "k"

# 문자 사이에 #가 없다면 k, v는 없음(v는 대각선으로 이동 못함)
"""
빈공간  빈공간  빈공간  울타리   빈공간   빈공간
빈공간  울타리  울타리  (늑대)   울타리  빈공간
울타리  (늑대)  빈공간  울타리   빈공간  울타리
울타리  빈공간  (양)    울타리  빈공간  울타리
빈공간  울타리  울타리  울타리   빈공간  울타리
빈공간  빈공간  빈공간  울타리   울타리  울타리
"""
# BFS(너비우선탐색)가 생각나는데..
# 해당 구역에서 양과 늑대의 생존 여부를 계산
# 울타리로 구획된 각 영역을 탐색
# 그 안에 양과 늑대 수를 비교하여 생존 여부 결정

from collections import deque

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    sheep, wolf = 0, 0

    if board[x][y] == 'k':
        sheep += 1
    elif board[x][y] == 'v':
        wolf += 1

    # 해당 위치는 이미 방문했으므로 표시
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위를 벗어나지 않고, 울타리가 아니며, 아직 방문하지 않은 경우
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and board[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

                # 양 또는 늑대를 만나면 카운트 증가
                if board[nx][ny] == 'k':
                    sheep += 1
                elif board[nx][ny] == 'v':
                    wolf += 1

    # 양이 늑대보다 많으면 늑대가 다 잡아먹힘, 그 외엔 양이 다 잡아먹힘
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

# 입력 처리
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

total_sheep = 0
total_wolf = 0

# 모든 좌표를 돌며 아직 방문하지 않은 빈 공간에서 BFS 수행
for i in range(R):
    for j in range(C):
        if not visited[i][j] and board[i][j] != '#':  # 울타리(#)가 아니고 방문하지 않은 곳
            sheep, wolf = bfs(i, j)
            total_sheep += sheep
            total_wolf += wolf

# 결과 출력: 살아남은 양과 늑대의 수6
print(total_sheep, total_wolf)
