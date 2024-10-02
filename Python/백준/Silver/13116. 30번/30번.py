# 문제) 
# 1023개의 꼭지점
# 1이 대응된 꼭지점에서 A가 대응된 꼭지점까지 가는 경로
# 1이 대응된 꼭지점에서 b가 대응된 꼭지점까지 가는 경로
# 공통으로 포함되는 꼭지점에 대응된 자연수 중 최대값 M(A,B)

# M(4, 11) = 2
# M(7, 12) = 3
# 10 * K

# 테스트 수 T
T = int(input())

for i in range(T):
    # A, B 입력받기
    A, B = map(int, input().split())

    # 부모노드를 찾을때까지 while문을 돌린다.
    while True:
        # A를 2로 나눈 몫
        if A > B:
            A = A // 2

        # B를 2로 나눈 몫
        elif A < B:
            B = B // 2

        # 반복되다가 A와 B가 같아지는 시점이 있다. 이때가 A,B의 부모노드임
        elif A == B:
            print(A * 10)
            break

