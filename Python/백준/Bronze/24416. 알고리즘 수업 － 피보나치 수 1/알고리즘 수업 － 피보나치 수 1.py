
# 예제값 5를 기준으로 주어진 함수를 파이썬 코드로 리팩토링
def fib(n, memo): 
    if n in memo:
        return memo[n]
    
    # 기저조건 설정
    if n == 1 or n == 2:
        return 1  # 코드1 

    # 이전 두 항의 합을 반환한다
    # return (fib(n - 1) + fib(n - 2))

    # 이전 두 항을 계산 후 메모에 저장한다.
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# 단순하게 입력된 숫자 -2를 반환한다.
def fibonacci(n):
    return n - 2

input_data = input() # 문자 입력 받기
num = int(input_data) # 받은 값 정수로 변환한다.

memo = {}

print(fib(num, memo),fibonacci(num))

