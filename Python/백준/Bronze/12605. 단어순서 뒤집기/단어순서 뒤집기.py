# 테스트 케이스 입력받기
# 스택으로 한번에 잘라서 입력받기
# 테스트 케이스 만큼 반복하여 테스트케이스 문자를 공백기준으로 split()
# 곧 바로 뒤집힌 값을 출력하기

import sys

# 테스트 케이스 수
N = int(input())

# 한번에 잘라서 입력받기
stack = list(map(str, sys.stdin.read().splitlines()))

# 테스트 케이스 수 만큼 반복
for i in range(N):
    # stack[i]는 하나의 케이스이며 이 문자열을 자른다.
    s = stack[i].split()
    # reversed해서 다시 합쳐준다.
    item = " ".join(reversed(s))
    print(f"""Case #{i+1}: {item}""")