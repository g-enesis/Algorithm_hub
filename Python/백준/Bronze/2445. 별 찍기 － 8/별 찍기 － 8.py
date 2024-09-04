"""
# 2024.09.04(수)
# 3번 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 예제 입력) 5
# 예제 출력)
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

input_data = input()

a = int(input_data)

for i in range(1, 2 * a):
    # i가 a보다 작거나 같으면 별을 점점 늘려가는 패턴
    if i <= a:
        left = '*' * i
        right = ' ' * (a - i)

    # i가 a보다 크면 별을 점점 줄여가는 패턴
    else:
        left = '*' * (2 * a - i)
        right = ' ' * (i - a)
    
    # 대칭 패턴으로 문자열을 붙여준다.
    print(left + right + right + left)
