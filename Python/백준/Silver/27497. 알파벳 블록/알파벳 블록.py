
import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  # N은 정수로 입력됨
blocks = deque()  # 문자열을 저장할 deque
history = []  # 추가된 블록 기록 (스택)

# 명령 처리
for i in range(1, N + 1):
    command = data[i].split()
    
    if command[0] == '1':
        # "1 c" : 맨 뒤에 블록 추가
        block = command[1]
        blocks.append(block)
        history.append(('1', block))  # 뒤에 추가된 기록을 저장
        
    elif command[0] == '2':
        # "2 c" : 맨 앞에 블록 추가
        block = command[1]
        blocks.appendleft(block)
        history.append(('2', block))  # 앞에 추가된 기록을 저장
        
    elif command[0] == '3':
        # "3" : 가장 나중에 추가된 블록 제거
        if history:
            last_action, last_block = history.pop()  # 히스토리에서 최근 기록을 꺼냄
            if last_action == '1':
                blocks.pop()  # 뒤에서 제거
            elif last_action == '2':
                blocks.popleft()  # 앞에서 제거

# 결과 출력
if blocks:
    print("".join(blocks))
else:
    print(0)
