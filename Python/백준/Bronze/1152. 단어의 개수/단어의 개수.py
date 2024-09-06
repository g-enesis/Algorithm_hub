# 입력받기
text = input()

# 입력받은 문자열을 공백단위로 쪼갠다.
text_split = text.split(" ")

# 개수를 셀 변수선언
count = 0

for t in text_split:
    # 쪼갠 단위의 길이값이 0인 텍스트를 제외하고 count를 증가시킨다.
    if(len(t) > 0): count = count + 1
   
print(count)