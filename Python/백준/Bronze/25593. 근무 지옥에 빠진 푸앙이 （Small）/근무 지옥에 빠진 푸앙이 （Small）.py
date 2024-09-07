
# 주의 개수 입력받기
n = int(input())

# 각 사람의 근무시간을 저장하는 딕셔너리
work_time = {}

# [근무 시간대에 따른 근무 시간]
# 08:00 ~ 12:00 = 4시간
# 12:00 ~ 18:00 = 6시간
# 18:00 ~ 22:00 = 4시간
# 22:00 ~ 08:00 = 10시간
shift_hours = [4, 6, 4, 10]


# 주(n) 수만큼 반복해서 근무표를 입력 받는다.
for _ in range(n):
    for shift in range(4): # 4개의 근무 시간대
        # 각 시간대에 근무하는 사람의 이름을 입력받는다.
        shifts = input().split()
        # print("\n")
        # print(shifts)
        # 여기까지 디버깅 결과.
        """
        ['-', '-', '-', '-', '-', 'sally', 'boss']
        ['-', '-', '-', '-', '-', 'brown', 'boss']
        ['-', '-', '-', '-', '-', 'moon', 'sally']
        ['-', '-', '-', '-', '-', 'leonard', 'edward']

        ['pangyo', 'moon', 'cony', 'boss', 'james', 'sally', 'brown']
        ['moon', 'brown', 'sally', 'cony', 'brown', 'choco', 'edward']
        ['moon', 'leonard', 'pangyo', 'moon', 'edward', 'puang', 'puang']
        ['leonard', 'sally', 'boss', 'choco', 'cony', 'boss', 'edward']

        ['brown', 'sally', 'jessica', 'leonard', 'moon', 'jessica', 'james']
        ['jessica', 'brown', 'leonard', 'puang', 'james', 'pangyo', 'puang']
        ['puang', 'choco', 'james', 'cony', 'jessica', 'pangyo', 'jessica']
        ['pangyo', 'jessica', 'choco', 'james', 'puang', 'cony', 'pangyo']

        ['moon', 'moon', 'james', 'choco', 'edward', '-', '-']
        ['jessica', 'brown', 'james', 'sally', 'puang', '-', '-']
        ['cony', 'leonard', 'moon', 'boss', 'choco', '-', '-']
        ['edward', 'jessica', 'cony', 'brown', 'leonard', '-', '-']
        """

        for person in shifts:
            # 만약 근무자가 있다면 진행 ('-'는 근무자가 없다는 의미이므로 제외시킨다.)
            if person != "-":
                # 상단에 선언한 work_time 딕셔너리에 근무자가 없다면
                if person not in work_time:
                    # 근무자를 추가하고 근무시간을 초기화해준다.
                    work_time[person] = 0

                # 초기화가 되고, 근무 시간을 더해준다.
                work_time[person] += shift_hours[shift]

# work_time을 찍어보면 아래처럼 딕셔너리가 채워진다.
# print(work_time)
"""
(ex)
    {
    'sally': 38, 
    'boss': 38, 
    'brown': 48, 
    'moon': 38, 
    'leonard': 48, 
    'edward': 44, 
    'pangyo': 38, 
    'cony': 48, 
    'james': 38, 
    'choco': 38, 
    'puang': 40, 
    'jessica': 48
    }
"""
# '아무도 근무하지 않을 경우 공평한 것으로 간주한다.' 라고 조건이 걸려있다.
# 그러므로 work_time의 길이가 0이라면 "Yes"
if len(work_time) == 0:
    print("Yes")

else:
    # [가장 많이] 근무한 사람의 근무시간 (work_time 딕셔너리 values들 중의 가장 큰 값)
    max_time = max(work_time.values())

    # [가장 적게] 근무한 사람의 근무시간 (work_time 딕셔너리 values들 중의 가장 작은 값)
    min_time = min(work_time.values())

    # (ex) 58, 14 (예제1의 근무테이블로 대입했을 경우)
    # print(max_time, min_time) 

    # 공평한 근무시간차 기준이 12시간 이하이므로 max_time - min_time 을 해준다. 
    if max_time - min_time <= 12:
        # 기준이 12시간 이하라면 "Yes"
        print("Yes")
    else:
        # 기준이 12시간 이하가 아니라면 "No"
        print("No")