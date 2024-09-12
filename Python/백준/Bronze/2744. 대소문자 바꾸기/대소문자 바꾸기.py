
# 문자 입력받기
input_data = input()

# 결과를 담을 변수
result = ""

# 입력받은 문자열을 list로 넣어 ["a","b","c"] 형태로 변환
for v in list(input_data):
    # 문자가 대문자일 경우 소문자로 
    if v.isupper():
        result += v.lower()
    # 문자가 소문자일 경우 대문자로 
    else:
        result += v.upper()

print(result)