import sys

input = sys.stdin.readline

n = int(input())
stack = []	
max_idx = [0,0]
for _ in range(n):
    info = list(map(int,input().split()))	
    if len(info) == 1:
        stack.pop(0)
    else:
        stack.append(info[1])

    student_idx = len(stack)
    if max_idx[0] < student_idx:
        max_idx[0] = student_idx
        max_idx[1] = stack[-1]
    elif max_idx[0] == student_idx:
        max_idx[1] = min(max_idx[1],stack[-1])

print(max_idx[0],max_idx[1])
 