# r = 31
# M = 1234567891(소수라는데 무슨말일까..)
# L = 입력(int)

L = int(input())
M = 1234567891
r = 31
user_input = input()
 
answer = 0
 
for i in range(L):
    # 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
    # ex) ord('a')를 넣으면 정수 97을 반환합니다.
    num = ord(user_input[i]) - 96

    # 힌트에 나와있는 공식
    answer += num * (r ** i)
 
print(answer % M)