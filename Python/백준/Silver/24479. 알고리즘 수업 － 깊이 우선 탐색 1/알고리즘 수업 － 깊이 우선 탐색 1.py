import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(current):
    global count
    visit[current] = count
    count += 1
    
    for neighbor in adj[current]:
        if visit[neighbor] == 0:
            dfs(neighbor)

# 입력 받기
data = input().split()
N, M, R = int(data[0]), int(data[1]), int(data[2])

# 그래프 인접 리스트
adj = [[] for _ in range(N + 1)]

# 간선 정보 받기
index = 3
for _ in range(M):
    u, v = int(data[index]), int(data[index + 1])
    adj[u].append(v)
    adj[v].append(u)
    index += 2

# 인접 리스트 오름차순 정렬
for i in range(1, N + 1):
    adj[i].sort()

# 방문 순서를 저장할 리스트
visit = [0] * (N + 1)

# 탐색 순서
count = 1

# DFS 탐색 시작
dfs(R)

# 방문 순서 출력
for i in range(1, N + 1):
    print(visit[i])
