# 문제 분석
# 뿅망치에 맞으면 키가 반으로 줄어든다.
# 단, 키가 1이면 더 줄어들지 않는다. 
# 뿅망치 횟수 제한이 있다. 
# 맨 처음은 가장 키가 큰 거인을 때린다.
# 이렇게 하면 모든 거인이 센티보다 키가 작을까? 

# 입력
# 첫째줄 거인 인구 수 N, 센티의 키, 뿅망치 횟수제한
# 두번째줄부터 거인의 키

# 로직
# 공백 기준으로 입력 받아서 n, height, num 에 담아주기
# 거인의 키를 리스트로 받고 heap에 저장
# 뿅망치 횟수 기준으로 반복문을 통해 거인의 키를 줄임


# 출력
# 센티보다 키가 작으면 첫째줄 YES, 두번째줄 뿅망치 최소 사용횟수
# 센티보다 키가 크거나 같으면 첫째줄 NO, 두번째줄 키가 가장 큰 거인의 키

import sys, heapq
input = sys.stdin.readline

n, h, t = map(int, input().split()) 
giants = [-int(input()) for _ in range(n)] # 거인의 키를 음수 값으로 리스트에 저장, 왜 음수? 최소 힙을 최대힙처럼 사용
heapq.heapify(giants) # 거인의 키를 heap 형태로 바꿔줌 [32, 16, 44] -> [16, 32, 44] default 최소 힙 
cnt = 0 

for i in range(t):
    if -giants[0] == 1 or -giants[0] < h: # 키가 1이거나 센티보다 키가 작으면 반복문 종료
        break
    else:
        heapq.heapreplace(giants, -(-giants[0] // 2))
        # 1. -giants[0](최대 값)을 2로 나눠줌
        # 2. 힙에 저장할때는 음수로 저장
        # 3. heapreplace : 힙에서 가장 작은 요소 제거 새로운 값 추가, 즉 새로운 값을 최소값으로 세팅
        cnt += 1

if -giants[0] >= h:
    print('NO', -giants[0], sep='\n')
else:
    print('YES', cnt, sep='\n')