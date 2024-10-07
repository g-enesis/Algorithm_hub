def dfs(graph, start, visited):
    visited[start] = True  # 현재 노드를 방문 처리
    count = 1  # 현재 컴퓨터도 바이러스에 걸리므로 1로 시작
    
    # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문
    for neighbor in graph[start]:
        if not visited[neighbor]:  # 방문하지 않은 컴퓨터일 경우
            count += dfs(graph, neighbor, visited)
    
    return count


# 입력
N = int(input())  # 컴퓨터의 수
M = int(input())  # 네트워크 상에서 직접 연결되어 있는 쌍의 수
graph = [[] for _ in range(N + 1)]  # 그래프 초기화

# 그래프 정보 입력 받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 방문 정보 초기화
visited = [False] * (N + 1)

# DFS를 사용하여 1번 컴퓨터로부터 바이러스에 걸린 컴퓨터 개수 구하기
infected_count = dfs(graph, 1, visited) - 1  # 1번 컴퓨터 제외

# 결과 출력
print(infected_count)
