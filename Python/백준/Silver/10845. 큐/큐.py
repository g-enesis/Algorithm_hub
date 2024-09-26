# 명령어 개수
# 스택 선언
# 명령어 공백으로 나누기
# 값이 있을 경우에만 저장

N = int(input())
S = []
results = []

for i in range(N):
    splitD = input().split()
    command = splitD[0]
    value = splitD[1] if len(splitD) > 1 else None

    if command == "push":
        # 정수를 큐에 넣는다.
        S.append(int(value))

    elif command == "pop":
        # 큐가 들어있는 정수가 있는 경우에는 그 수
        if S:
            results.append(S.pop(0))
        # 만약 큐가 들어있는 정수가 없는 경우에는 -1
        else:
            results.append(-1)

    elif command == "size":
        # 큐에 들어있는 요소 개수
        results.append(len(S))

    elif command == "empty":
        # 큐가 비어있으면 1, 아니면 0
        results.append(1 if not S else 0)

    elif command == "front":
        # 큐에 가장 앞의 정수
        if S:
            results.append(S[0])
        # 정수가 없다면 -1
        else:
            results.append(-1)

    elif command == "back":
        # 큐에 가장 뒤의 정수
        if S:
            results.append(S[-1])
        # 정수가 없다면 -1
        else:
            results.append(-1)

for result in results:
    print(result)