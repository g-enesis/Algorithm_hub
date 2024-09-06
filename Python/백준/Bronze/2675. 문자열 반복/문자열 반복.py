
T = int(input())

# 테스트 케이스 반복문
for i in range(T):
    # 문자열 전달
    input_data = input()
    
    # 입력받기
    n, s = input_data.split(" ")
    N, S = int(n), s
    
    # 문자열 담을 변수
    text = ""

    # 문자열 1개씩 * N한 값을 text에 붙인다.
    for j in S:
        text += j * N

    print(text)