
# 정수의 개수(=반복)
N = int(input())

lists = list(map(int, input().split()))

# 최댓값과 최솟값을 구하기 위한 기본 값 넣어주기(0은 안됌)
maxNum, minNum = lists[0],lists[0]

for i in range(0, N):
    # 최댓값
    if lists[i] > maxNum:
        maxNum = lists[i]
        
    # 최솟값
    if lists[i] < minNum:
        minNum = lists[i]

print(minNum, maxNum)