from collections import deque

def find_brother(N, K):
    # 최대 좌표는 100,000이므로 이를 포함할 수 있는 크기로 설정
    max_pos = 100000
    # 방문한 위치와 시간을 기록할 리스트
    visited = [-1] * (max_pos + 1)

    # BFS를 위한 큐 초기화
    queue = deque([N])
    visited[N] = 0  # 시작점은 0초

    # BFS 실행
    while queue:
        current_pos = queue.popleft()

        # 동생을 찾으면 현재 위치의 시간을 반환
        if current_pos == K:
            return visited[current_pos]

        # 세 가지 이동 방식에 대해 BFS 확장
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            # 다음 위치가 범위 내에 있고 아직 방문하지 않은 경우에만 처리
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[current_pos] + 1
                queue.append(next_pos)

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(find_brother(N, K))
