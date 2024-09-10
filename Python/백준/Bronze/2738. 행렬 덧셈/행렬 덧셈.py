n, m = map(int, input().split())  # 행렬의 크기 N과 M 입력받기

# 빈 리스트 A와 B 초기화
A = []
B = []

# 행렬 A 입력받기
for i in range(n):
    A.append(list(map(int, input().split())))

# 행렬 B 입력받기
for i in range(n):
    B.append(list(map(int, input().split())))

# 두 행렬을 더한 결과 출력
for i in range(n):
    result = []
    for j in range(m):
        result.append(A[i][j] + B[i][j])  # A와 B의 같은 위치 값 더하기
    print(' '.join(map(str, result)))  # 결과를 공백으로 구분해서 출력
