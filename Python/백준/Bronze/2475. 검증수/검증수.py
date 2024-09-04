# 사용자의 입력을 받아들입니다. 이 입력은 기본적으로 문자열 형태로 들어온다.
input_data = input()

# 입력된 문자열을 공백 기준으로 나누어 리스트로 변환한다.
a,b,c,d,e = input_data.split(" ")

# 문자열을 정수로 변환한다
A,B,C,D,E = int(a),int(b),int(c),int(d),int(e)

# 계산이 잘 되는지 확인 Ex) 0 16 4 25 36
# print(A*A,B*B,C*C,D*D,E*E)

# 검증수는 A,B,C,D,E를 전부 합한 값을 10으로 나눈 나머지이므로 계산을 해준다.
result = sum([A*A,B*B,C*C,D*D,E*E]) % 10

# 결과 확인 Ex) 1
print(result)