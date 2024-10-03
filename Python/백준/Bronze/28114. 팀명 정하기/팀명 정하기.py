""" 
성서의 가이드라인에 따르면 팀 이름을 짓는 방법은 두 가지가 있다.

 1.세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열
 2.세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열

 예를 들어 
 600문제를 해결한 18학번 안(AHN)씨, 
 2000문제를 해결한 19학번 이(LEE)씨, 
 6000문제를 해결한 20학번 오(OH)씨로 구성된 팀을 생각해 보자. 
 
 첫 번째 방법으로 팀명을 만들면 181920이 되고, 
 두 번째 방법으로 팀명을 만들면 OLA가 된다.

 2000문제를 해결한 19학번 이(LEE)씨, 
 9000문제를 21학번 나(NAH)씨, 
 1000문제를 해결한 22학번 박(PARK)씨로 구성된 팀은 

 첫 번째 방법으로 팀명을 만들면 192122가 되고, 
 두 번째 방법으로 팀명을 만들면 NLP가 된다.

 세 팀원의 백준 온라인 저지에서 
 해결한 문제의 개수, 
 입학 연도, 
 그리고 성씨가 주어지면
  첫 번째 방법과
  두 번째 방법으로 만들어지는 팀명을 차례대로 출력하는 프로그램을 작성하라.
  """

# print(2018%100)
# print(2019%100)
# print(2020%100)

# print("AHN"[0])
# print("LEE"[0])
# print("OH"[0])

# 1.세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열
# def solution_1(dict=dict):
#     array = []
#     for key, value in dict.items():
#         year = int(value[1]) % 100
#         array.append(year)

#     for i in range(len(array)):
#         min_index = i # 가장 작은 원소의 인덱스
#         for j in range(i + 1, len(array)):
#             if array[min_index] > array[j]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i] # 스와프

#     print(array)
#     return array

# # 2.세 참가자 중 성씨를 영문으로 표기했을 때의 
# # 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열
# def solution_2(dict=dict):
#     print("dict2: ", dict)
#     result = []
#     for key, value in dict.items():
#         solved, name = int(value[0]), str(value[2])
#         print("solved: ", solved)
#         print("name: ", name)

# dict = {}

# # 출력
# for i in range(3):
#     # 입력받기
#     input_data = input().split()
#     dict[i] = input_data

# solution_1(dict)
# solution_2(dict)
sol1 = []
rank_dict = {}

for i in range(3):
    input_data = input().split()
    solved, year, name = input_data[0],input_data[1],input_data[2]
    
    sol1.append(int(year) % 100)
    rank_dict[name] = int(solved)

# 선택 정렬 알고리즘으로 sol1을 정렬
for i in range(len(sol1)):
    # 가장 작은 원소의 인덱스
    min_index = i 

    for j in range(i + 1, len(sol1)):
        if sol1[min_index] > sol1[j]:
            min_index = j

    sol1[i], sol1[min_index] = sol1[min_index], sol1[i]  # 스와프

# 딕셔너리의 항목을 리스트로 변환
items = list(rank_dict.items())

# bubble sort 알고리즘을 사용하여 값 기준으로 내림차순 정렬
for i in range(len(items)):
    for j in range(len(items) - i - 1):
        if items[j][1] < items[j + 1][1]:  # 값을 비교하여 스왑
            items[j], items[j + 1] = items[j + 1], items[j]

# 정렬된 리스트를 딕셔너리로 변환
sol2 = ""
for key, value in items:
    sol2 += key[0]  # 첫 글자만 추출

print(*sol1, sep="")  # 정렬된 연도를 출력
print(sol2)  # 정렬된 이름의 첫 글자를 출력
