
# 문자 입력받기
A = input().split()
B = input().strip()

# 접두사 갯수 count 선언
count = 0

for text in A:
    # 문자값이 동일하지 않고 text앞에 붙는 문자가 포함되어있는지 확인한다.(접두사)
    if text != B and text.startswith(B):
        count += 1 # count 증가


print(count)