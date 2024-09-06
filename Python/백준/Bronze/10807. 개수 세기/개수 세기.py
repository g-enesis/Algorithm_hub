
# N개의 정수 입력받기
N = int(input())

# 주어진 문자열을 int로 변환 후 리스트에 담기
int_nums = list(map(int, input().split()))
 
# 비교할 값 입력받기
V = int(input())

# 찾은 개수
count = 0

# 정수(N) 만큼 반복한다.
for i in range(N):
    # 입력받은 비교하는 값과 int_nums의 i번째를 순차적으로 비교
    if V == int_nums[i]:
        # 찾았다면(같으면) +1
        count += 1

print(count)

