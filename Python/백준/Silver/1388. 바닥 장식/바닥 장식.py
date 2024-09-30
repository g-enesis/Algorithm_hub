def count_planks(N, M, floor):
    # 방문한 칸을 체크하는 배열
    visited = [[False] * M for _ in range(N)]
    count = 0

    # 가로로 나무 판자 세기 ('-')
    for i in range(N):
        for j in range(M):
            if floor[i][j] == '-' and not visited[i][j]:
                # 새로운 나무 판자 발견
                count += 1
                # 가로로 연속된 '-' 처리
                k = j
                while k < M and floor[i][k] == '-':
                    visited[i][k] = True
                    k += 1

    # 세로로 나무 판자 세기 ('|')
    for i in range(N):
        for j in range(M):
            if floor[i][j] == '|' and not visited[i][j]:
                # 새로운 나무 판자 발견
                count += 1
                # 세로로 연속된 '|' 처리
                k = i
                while k < N and floor[k][j] == '|':
                    visited[k][j] = True
                    k += 1

    return count

# 입력
N, M = map(int, input().split())
floor = [input().strip() for _ in range(N)]

# 결과 출력
print(count_planks(N, M, floor))
