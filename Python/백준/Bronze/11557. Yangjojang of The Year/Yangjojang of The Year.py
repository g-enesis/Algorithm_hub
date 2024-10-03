# 첫 줄 = 테스트 수
# 테스트 내 첫 줄 = 학교의 숫자
# 테스트 내 N 줄 = 학교이름, 소비한 술의 양

# 테스트 케이스 수
T = int(input())

for i in range(T):
    schools = int(input())
    
    consume_dict = {}

    for j in range(schools):
        split_items = input().split()
        school_name, consume_rum = str(split_items[0]), int(split_items[1])

        consume_dict[school_name] = consume_rum
    
    # 딕셔너리의 항목을 리스트로 변환
    items = list(consume_dict.items())

    # bubble sort 알고리즘을 사용하여 값 기준으로 내림차순 정렬
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:  # 값을 비교하여 스와프
                items[j], items[j + 1] = items[j + 1], items[j]


    # 가장 많이 술을 소비한 학교 출력
    # items[0]이 가장 많은 소비량을 가진 학교임
    print(items[0][0])  # 학교 이름 출력
