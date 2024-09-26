
# 막대기 개수를 N 으로 선언.
# 막대기 높이에 대한 입력값을 스택에 순서대로 추가한다.
# 맨 뒤에 추가된 값을 기준으로 잡아 변수로 선언해놓기.
# 맨 뒤에 추가된 값보다 크면 카운팅하고 그 값으로 치환, 작거나 같으면 카운팅하지 않는다.

import sys

# 막대기 개수 N
N = int(input())

# 시간초과를 염두하여 입력을 한 번에 받아서 처리
stack = list(map(int, sys.stdin.read().split()))

# 카운팅되는 막대기 값(마지막 막대는 무조건 보이므로 1로 초기화)
count = 1

# 스택의 마지막 막대 값
stack_max = stack[-1]

# 오른쪽에서 왼쪽으로 비교(맨 마지막은 이미 포함되어 있으므로 그 전부터 비교)
for i in range(N-2, -1, -1):
    # 스택 마지막값 기준 순차적으로 비교
    if stack[i] > stack_max:
        # 카운팅 +1
        count += 1
        # 갈아껴주기
        stack_max = stack[i]
        
print(count)



