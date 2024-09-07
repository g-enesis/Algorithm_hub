
# 입력받기
count = int(input())

# 뽑을번호 리스트
nums = list(map(int, input().split()))


# 최종적으로 줄을 선 순서를 저장할 리스트
result = []

# i는 학생 번호 (1번부터 시작), v는 뽑은 번호
for i, v in enumerate(nums, start=1):
    # 각 학생은 뽑은 번호(v)만큼 앞으로 이동하므로 
    # result에 i(번째학생)를 
    # len(result) - v(result의 현재 길이 - 뽑은 번호(만큼)) 위치에 삽입
    result.insert(len(result) - v, i)

print(' '.join(map(str, result)))