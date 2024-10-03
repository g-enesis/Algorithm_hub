# HCPC 티켓의 번호가 작을수록 목소리를 가까이에서 들을 수 있다.

# 양한이의 티켓팅(1차 티켓팅에서 이미 팔린 티켓의 번호 목록 = 1번부터 시작)
# 첫째 줄 = 1차 티켓팅에서 팔린 티켓들의 수 N
# 둘째 줄 = 1차 티켓팅에서 팔린 티켓들의 번호 Aj
# 1차 티켓팅이 끝난 번호들을 제외
# 가장 작은 번호 출력

# 팔린 티켓 수
N = int(input())

# 팔린 티켓 번호목록

# A = list(map(int , input().split()))
# 시간초과로 인해 set으로 변경
A = set(map(int , input().split()))

# 1번부터 시작
ticket_number = 1

# 범위를 한정할 수 없기때문에 
# while문으로 ticket_number와 균일하도록 ticket_number를 +1 한다.
while ticket_number in A:
    ticket_number = ticket_number + 1
    # while 루프를 돌다가 ticket_list에 포함되있지 않는 
    # 가장 첫 작은 번호를 출력하는 것이기 때문에 루프를 종료된다.
print(ticket_number)