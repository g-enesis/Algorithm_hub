def compute_at_operator(A, B):
    """
    A @ B를 계산하는 함수
    :param A: 첫 번째 정수
    :param B: 두 번째 정수
    :return: 연산 결과
    """
    return (A + B) * (A - B)


import sys
input = sys.stdin.read
data = input().strip()

# 입력을 읽어와서 정수 A와 B로 변환
A, B = map(int, data.split())

# A @ B 계산
result = compute_at_operator(A, B)

# 결과 출력
print(result)