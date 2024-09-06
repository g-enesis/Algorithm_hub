# 출석번호 1~30번 까지 생성
student = list(range(1, 31))

for n in range(1, len(student)-1):
    # 제출한 학생의 출석번호를 입력받는다.
    work = int(input())

    # 입력받은 출석번호를 제외시킨다.
    student.remove(work)

# 출석번호 중 가장 작은 것을 출력한다.
print(min(student))

# 가장 작은 출석번호도 제외시킨다.
student.remove(min(student))

# 남은 출석번호는 1개, 리스트 압축을 해제한다.
print(*student)