# 최단거리 구하기
# 그림을 보았을 때 BFS로 풀라는 뉘앙스
# 나이트는 몇 번 움직이면 저 초록칸에 이동할 수 있는지
# BFS는 선입선출(FIFO)
"""
- BFS를 사용하여 현재 위치에서 목표 위치로 이동하는 최소 횟수를 구합니다.
- BFS는 큐를 사용하며, 현재 위치에서 나이트가 이동할 수 있는 8방향을 탐색합니다.
- 목표 위치에 도착하면 탐색을 종료하고, 이동 횟수를 출력합니다.
"""
from collections import deque

# 나이트의 이동 방향 (총 8방향)
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# BFS 함수: start에서 end까지 최소 이동 횟수를 구함
def bfs(l, start_x, start_y, end_x, end_y):
    # 방문 여부를 체크하는 배열 (l x l 크기)
    # visited = [[False] * l for _ in range(l)]
    visited = []

    for _ in range(l):
        row = []
        for _ in range(l):
            row.append(False)
        visited.append(row)
        
    queue = deque([(start_x, start_y, 0)])  # 큐에는 (x좌표, y좌표, 이동횟수)를 저장
    visited[start_x][start_y] = True
    
    while queue:
        # print(queue)
        x, y, moves_count = queue.popleft()
        # print("x: ", x)
        # print("y: ", y)
        # print("moves_count: ", moves_count)
        # print("queue: ", queue)
        
        # 목표 위치에 도착하면 이동 횟수를 반환
        if x == end_x and y == end_y:
            return moves_count
        
        # 나이트가 이동할 수 있는 8방향을 모두 탐색
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            # 체스판 내에 있고, 아직 방문하지 않은 칸이면 이동
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves_count + 1))
    
    return -1  # 목표 위치에 도달할 수 없는 경우는 없으므로 필요하지 않음

# 입력 받기
t = int(input())  # 테스트 케이스 수

for _ in range(t):
    l = int(input())  # 체스판의 크기
    start_x, start_y = map(int, input().split())  # 나이트의 시작 위치
    end_x, end_y = map(int, input().split())  # 나이트의 목표 위치
    
    # 나이트의 시작 위치와 목표 위치가 같으면 0을 출력
    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        # BFS를 통해 최소 이동 횟수를 구해서 출력
        print(bfs(l, start_x, start_y, end_x, end_y))
