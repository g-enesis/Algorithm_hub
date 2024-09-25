import sys

# 표준 입력을 모두 읽어들인 후, 줄 단위로 데이터를 나누어 리스트로 저장
input = sys.stdin.read
data = input().splitlines()

# 괄호의 균형을 확인하는 함수
def check_balance(s):
    stack = []  # 스택을 사용하여 괄호의 균형을 확인하기 위해 빈 리스트로 초기화
    for char in s:  # 문자열의 각 문자를 하나씩 확인
        if char == "(" or char == "[":  # 만약 '(' 또는 '['가 나오면
            stack.append(char)  # 스택에 추가하여 쌓음
        elif char == ")":  # 만약 ')'가 나오면
            # 스택이 비어 있거나, 스택의 마지막 요소가 '('가 아니면 균형이 맞지 않음
            if not stack or stack[-1] != "(":
                return "no"  # 균형이 맞지 않으므로 "no" 반환
            stack.pop()  # 짝이 맞는 '('를 제거 (스택에서 팝)
        elif char == "]":  # 만약 ']'가 나오면
            # 스택이 비어 있거나, 스택의 마지막 요소가 '['가 아니면 균형이 맞지 않음
            if not stack or stack[-1] != "[":
                return "no"  # 균형이 맞지 않으므로 "no" 반환
            stack.pop()  # 짝이 맞는 '['를 제거 (스택에서 팝)
    
    # 문자열을 모두 처리한 후 스택이 비어있다면 괄호가 모두 짝이 맞는 것임
    if not stack:  # 스택이 비어 있다면
        return "yes"  # 균형이 맞으므로 "yes" 반환
    else:  # 스택에 남아있는 괄호가 있다면 균형이 맞지 않음
        return "no"  # 균형이 맞지 않으므로 "no" 반환

# 입력된 데이터에서 한 줄씩 처리
for line in data:
    if line == ".":  # 만약 한 줄이 '.'만 있다면 입력의 끝을 의미하므로 종료
        break
    print(check_balance(line))  # 각 줄에 대해 균형 확인 결과를 출력
