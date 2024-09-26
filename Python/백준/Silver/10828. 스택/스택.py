# 명령어개수 입력받기
# 스택 선언
# 명령어 공백으로 나누기
# 값이 있을 경우에만 저장

N, S, result = int(input()), [], []

for i in range(N):
    splitD = input().split()
    command = splitD[0]
    value = splitD[1] if len(splitD) > 1 else None

    # 정수를 스택에 넣는다.
    if command == "push":
        S.append(int(value))

    # 스택에서 가장 위에 있는 정수를 빼고 그 수 출력
    elif command == "pop":
        if S:
            result.append(S.pop(-1))
        # 스택에 들어있는 정수가 없으면 -1
        else:
            result.append(-1)

    # 스택에 들어있는 정수의 개수 출력
    elif command == "size":
        result.append(len(S))
    
    # 스택이 비어있다면 1 아니면 0
    elif command == "empty":
        if S:
            result.append(0)
        else:
            result.append(1)

    # 스택의 가장 위에 있는 정수 출력
    elif command == "top":
        if S:
            result.append(S[-1])
        # 스택에 들어있는 정수가 없으면 -1
        else:
            result.append(-1)

for res in result:
    print(res)
