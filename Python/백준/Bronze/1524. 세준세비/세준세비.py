# 세준이와 세비의 온라인게임

# 세준: N명의 병사
# 세비: M명의 병사

# 전쟁은 여러번
# 살아있는 제일 약한 병사는 죽는다. = 가장 작은 수 제외
# 제일 약한 병사가 여러명이고 모두 같은 편에 있다면 그 중에 임의로 한명이 죽는다.
# 양 편에 모두 있다면, 세비의 제일 약한 병사 중 임의로 한명이 죽는다.

# 테스트 수 T
# 각 테스트
#  - 첫째 줄: N M
#  - 둘째 줄: 세준이의 병사들의 힘
#  - 셋째 줄: 세비의 병사들의 힘

# 클수록 강하고, 작을수록 약함

# 선택 정렬 함수
# def sort_func(user):
#     for i in range(len(user)):
#         min_index = i # 가장 작은 원소의 인덱스
#         for j in range(i + 1, len(user)):
#             if user[min_index] > user[j]:
#                 min_index = j
#         user[i], user[min_index] = user[min_index], user[i] # 스와프

 

# 테스트 수
T = int(input())

for i in range(T):
    input()
    # N명의 세준병사, M명의 세비병사
    N, M = map(int, input().split())

    # 세준 병사들의 힘
    sj = sorted(list(map(int, input().split())), reverse=True)

    # 세비 병사들의 힘
    sb = sorted(list(map(int, input().split())), reverse=True)
    
    while sj and sb:
        if sj[-1] >= sb[-1]: 
            sb.pop()

        else: 
            sj.pop()

    # 세준 승리
    if sj :
        print('S')

    # 세비 승리
    elif sb :
        print('B')
    
    # 둘 다 전멸(세준, 세비 힘 리스트가 둘 다 0일 때)
    else :
        print('C')

