   
# 문자열 입력받기
T = input()

# 공백기준 나누어 각 a, b에 저장
a, b = map(str, T.split())

# a, b를 리스트로 변환 후 A, B에 저장
A, B = list(a), list(b)

# a, b 각각 reversed로 역순 변환 후 join으로 하나의 문자열로 합친다.
# 하나의 문자열이 된 값을 정수형(int)으로 변환
parse_A = int(''.join(reversed(a)))
parse_B = int(''.join(reversed(b)))

# max 함수로 이터러블한 값을 전달하여 최대값 산출
result = max([parse_A, parse_B])

print(result)