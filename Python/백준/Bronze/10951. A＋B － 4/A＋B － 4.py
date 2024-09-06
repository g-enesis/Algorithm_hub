
# 여러개의 테스트케이스 정의
while 1:
    try:
        # 문자 입력받아 정수로 변환 후 A, B로 저장
        A, B = map(int, input().split())
        print(A + B)
    except:
        break