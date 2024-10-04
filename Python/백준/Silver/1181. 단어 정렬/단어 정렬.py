
# N개의 단어
#  - 길이가 짧은 순
#  - 길이가 같다면 사전 순

N = int(input())

word = []

for _ in range(N):
    w = input()
    # 중복된 데이터 중 하나는 남겨야한다.
    # 따라서 중복된 데이터가 없을 때 추가
    if w not in word:
       word.append(w)

# 길이가 짧은 순으로 정렬하고, 길이가 같으면 사전순으로 정렬
sorted_word = sorted(word, key=lambda w: (len(w), w))
# lambda x: (len(x), x)는 x라는 단어에 대해 그 단어의 (길이, 단어)를 반환하는 함수입니다.
# sorted() 함수는 이 반환값을 기준으로 먼저 길이를 기준으로 정렬하고, 길이가 같으면 단어 자체를 사전 순으로 정렬합니다.

for sw in sorted_word:
    print(sw)

# lambda
"""
def add(a, b):
    return a + b

lambda 
> add = lambda a, b: a + b

lambda arguments: expression
- arguments : 함수에 전달되는 매개변수
- expression : 리턴되는 값(단일 표현식)
"""