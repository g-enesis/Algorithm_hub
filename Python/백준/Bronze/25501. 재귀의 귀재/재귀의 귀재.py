
count = 0 # 재귀 함수 호출 횟수를 저장하는 변수

def recursion(s, l, r):
    global count # 전역 변수 count를 사용하기 위해 global 키워드 사용
    count += 1 # 함수 호출할 때마다 count를 1씩 증가

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count # 전역 변수 count를 사용하기 위해 global 키워드 사용
    count = 0 # 새로운 회문 검사를 시작할 때 count를 0으로 초기화

    return recursion(s, 0, len(s)-1) # 재귀 함수를 호출하여 회문 여부를 반환

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 회문 여부와 재귀 호출 횟수 출력
for i in range(T):
    S = input()  # 알파벳 대문자로 구성된 문자열 입력
    # isPalindrome 함수로 회문 여부를 검사하고, 호출 횟수를 함께 출력
    print(isPalindrome(S), count)
