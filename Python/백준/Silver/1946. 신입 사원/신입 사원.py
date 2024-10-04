import sys

input = sys.stdin.readline

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 지원자 수 입력
    N = int(input())
    
    # 지원자들의 서류심사, 면접 성적 입력 받기
    rank = [list(map(int, input().split())) for _ in range(N)]
    
    # 서류 심사 성적을 기준으로 오름차순 정렬
    rank.sort(key=lambda x: x[0])
    
    # 면접 성적에서 비교할 기준을 첫 번째 지원자의 면접 성적으로 설정
    top_interview = rank[0][1]
    
    # 첫 번째 지원자는 서류 성적 1등이므로 무조건 선발 (최소 1명은 선발)
    result = 1

    # 두 번째 지원자부터 면접 성적을 비교하며 선발 여부 결정
    for i in range(1, N):
        # 현재 지원자의 면접 성적이 현재까지 최고 면접 성적보다 좋으면 선발 가능
        if rank[i][1] < top_interview:
            result += 1
            # 선발되었으므로, 새로운 최고 면접 성적을 업데이트
            top_interview = rank[i][1]
    
    # 각 테스트 케이스에 대한 결과 출력
    print(result)
