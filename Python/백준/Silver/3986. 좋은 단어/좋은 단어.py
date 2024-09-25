N = int(input())

result = 0

for _ in range(N):
    stack = []
    lists = list(input())
    # print(lists)
    for i in lists:
        # stack 이 비어있을 때만 true >>> len(stack) == 0
        if not len(stack):
            # stack 이 비어있을 때만 i를 스택에 추가
            stack.append(i)
            # print("1번: ",stack)
        
        # stack 의 마지막 요소값이 현재 진행하는 값과 동일한지 체크
        elif stack[-1] == i:
            # 참일 때 마지막 요소 제거
            stack.pop(-1)
            # print("2번: ",stack)
        
        # 현재 요소값을 stack에 추가
        else:
            stack.append(i)
            # print("3번: ",stack)

    # print(lists)    
    # print(stack)

    if not len(stack):
        result += 1

print(result)