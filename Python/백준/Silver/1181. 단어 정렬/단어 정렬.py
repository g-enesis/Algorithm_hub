
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
sorted_word = sorted(word, key=lambda x: (len(x), x))

for sw in sorted_word:
    print(sw)