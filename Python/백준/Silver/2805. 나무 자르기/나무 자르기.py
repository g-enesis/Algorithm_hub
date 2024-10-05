def get_cut_wood(trees, height):
    """주어진 높이에서 잘린 나무의 총 길이를 계산하는 함수"""
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def find_max_height(trees, M):
    """이분 탐색을 이용해 적어도 M미터의 나무를 가져갈 수 있는 절단기의 최대 높이를 찾는 함수"""
    low, high = 0, max(trees)  # 절단기의 높이는 0부터 최대 나무 높이까지 가능
    
    result = 0
    while low <= high:
        mid = (low + high) // 2  # 중간값 (절단기의 높이)
        cut_length = get_cut_wood(trees, mid)  # 이 높이에서 잘린 나무의 길이
        
        if cut_length >= M:
            result = mid  # 가능한 경우, 더 큰 높이도 시도해본다
            low = mid + 1
        else:
            high = mid - 1  # 잘린 나무의 길이가 부족하므로 높이를 줄인다
    
    return result

# 입력 받기
N, M = map(int, input().split())  # 나무의 수 N, 필요한 나무의 길이 M
trees = list(map(int, input().split()))  # 나무의 높이

# 절단기의 최대 높이 구하기
max_height = find_max_height(trees, M)

# 결과 출력
print(max_height)
