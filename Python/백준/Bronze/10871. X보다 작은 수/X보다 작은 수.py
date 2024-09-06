
# 문자열 입력받아 정수형으로 변환(N:반복값, X:비교값)
N, X = map(int, input().split())

# 수열 입력받기
A = input().split()

# 입력받은 수열 int형 리스트로 변환
int_A = list(map(int, A))

# 결과 리스트 변수선언
result = []

# 반복값(N)만큼 반복
for i in range(N):
    # 비교값(X)보다 수열(int형)이 작을 경우 
    if X > int_A[i]:
        # 결과 리스트 변수에 추가
         result.append(str(int_A[i]))

# 공백을 추가하여 합치기
print(' '.join(result)) 