def can_reach_goal(N, board):
    # DFS를 사용하기 위한 스택
    stack = [(0, 0)]  # 출발점 (0, 0)에서 시작
    visited = [[False] * N for _ in range(N)]  # 방문 여부 체크

    # DFS로 탐색
    while stack:
        x, y = stack.pop()

        # 목표 지점에 도달하면 "HaruHaru" 출력
        if board[x][y] == -1:
            return "HaruHaru"

        # 이미 방문한 칸이면 패스
        if visited[x][y]:
            continue

        visited[x][y] = True  # 방문 처리
        jump = board[x][y]  # 현재 칸에서 이동할 수 있는 거리

        # 오른쪽으로 이동
        if y + jump < N and not visited[x][y + jump]:
            stack.append((x, y + jump))

        # 아래로 이동
        if x + jump < N and not visited[x + jump][y]:
            stack.append((x + jump, y))

    # 끝까지 도달하지 못한 경우 "Hing" 출력
    return "Hing"

# 입력 처리
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(can_reach_goal(N, board))
