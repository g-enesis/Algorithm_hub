# N개의 노래정보 입력받음
# 첫 세 음이 포함된 노래가 여러 개이면 "?" 출력
# 노래정보 중 입력한 첫 세 음에 맞는 노래가 없다면 "!" 출력
# 대문자와 소문자 구분

# N : 정환이 음을 아는 노래의 개수 
# M : 정환이 맞히기를 시도할 노래의 개수(공백으로 구분)
N, M = map(int, input().split())

# 화음을 담을 딕셔너리
music = {}

# TODO N >> 정환이 아는 노래의 개수 for
for i in range(N):
    input_data = input().split()

    # T: 노래 제목의 길이
    # S: 노래 제목
    T, S = int(input_data[0]), str(input_data[1])

    # 노래제목, 화음 첫 세 음 저장
    music[S] = input_data[2:5]

# TODO M >> 정환이 맞히기를 시도할 노래의 개수 for
for i in range(M):
    input_data = input().split()
    # 같은 노래 개수 카운트, 노래 제목 변수
    count, title = 0, ""

    # 화음 담긴 딕셔너리를 풀어서 입력받은 화음과 비교
    for s in music:
        # 같다면
        if input_data == music[s]:
            # 같은 노래 개수 +1
            count += 1
            # 노래제목 저장
            title = s

    # 같은 노래가 2개 이상
    if count >= 2:
        print("?")

    # 같은 노래가 1개만 있다면
    elif count == 1:
        print(title)

    # 같은 노래가 없다면
    else:
        print("!")


# print("N: ", N)
# print("M: ", M)
# print("T: ", T)
# print("S: ", S)