from collections import deque

N = int(input())  # 명령의 수
D = deque()  # 덱 초기화

# 결과를 저장할 리스트
results = []

for _ in range(N):
    splitD = input().split()  # 명령어를 공백으로 나누기
    command = splitD[0]  # 명령어
    value = splitD[1] if len(splitD) > 1 else None  # 값이 있을 경우에만 저장

    # push_front X: 정수 X를 덱의 앞에 넣는다.
    if command == "push_front":
        D.appendleft(int(value))  # 정수를 덱의 앞에 추가

    # push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif command == "push_back":
        D.append(int(value))  # 정수를 덱의 뒤에 추가

    # pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "pop_front":
        if D:
            results.append(D.popleft())  # 가장 앞의 수를 빼고 결과 저장
        else:
            results.append(-1)  # 덱이 비어있으면 -1 저장

    # pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "pop_back":
        if D:
            results.append(D.pop())  # 가장 뒤의 수를 빼고 결과 저장
        else:
            results.append(-1)  # 덱이 비어있으면 -1 저장

    # size: 덱에 들어있는 정수의 개수를 출력한다.
    elif command == "size":
        results.append(len(D))  # 덱의 크기 저장

    # empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command == "empty":
        results.append(1 if not D else 0)  # 비어있으면 1, 아니면 0 저장

    # front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "front":
        if D:
            results.append(D[0])  # 가장 앞의 수 저장
        else:
            results.append(-1)  # 덱이 비어있으면 -1 저장

    # back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif command == "back":
        if D:
            results.append(D[-1])  # 가장 뒤의 수 저장
        else:
            results.append(-1)  # 덱이 비어있으면 -1 저장

# 모든 결과를 한 번에 출력
for result in results:
    print(result)
