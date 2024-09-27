# 단어의 수 만큼 반복
# 반복문에서 단어를 입력받고 해시테이블에 저장
# 해시테이블에서 역순 단어 존재하면 출력 로직
# 길이 식, 가운데 문자 식 

# 단어의 수 입력받음
N = int(input())

# 해시테이블 정의
hash_table = {}

# 단어의 수 만큼 반복
for i in range(N):
    # 단어 입력받기
    word = input()

    # 단어 저장
    hash_table[word] = word
  
    # 뒤집어진 단어
    reversed_word = word[::-1]

    # 뒤집어진 단어가 존재하면 출력
    if reversed_word in hash_table:
        length = len(word) # 첫째 줄 단어의 비밀번호 길이
        middle_string = word[length // 2] # 첫째 줄 단어의 가운데 글자
        print(length, middle_string)


# print(hash_table)
# 31120kb, 36ms