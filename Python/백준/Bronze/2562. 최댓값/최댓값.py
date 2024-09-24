# 빈 딕셔너리 생성
numbers_dict = {}

# 9개의 입력을 받아서 딕셔너리에 저장 (key: 입력 값, value: 해당 값의 위치)
for i in range(9):
    num = int(input())  # 입력받은 숫자를 정수로 변환
    numbers_dict[num] = i + 1  # 딕셔너리에 숫자와 그 위치 저장 (위치는 1부터 시작)


# 딕셔너리에서 최댓값을 구함
max_value = max(numbers_dict)

# 최댓값과 그 값의 위치를 출력
print(max_value)
print(numbers_dict[max_value])
