
# 문자열 입력받기
S = input()

# i번째 입력받고 정수로 변환
N = int(input())

# 문자열을 리스트에 넣어 ["",""..]로 변환
lists = list(S)

# N-1 ~ N까지 문자를 지정하고 리스트를 해체
print(*lists[N-1:N])