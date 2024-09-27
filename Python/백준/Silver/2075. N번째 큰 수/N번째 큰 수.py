import heapq

n = int(input())
min_heap = [] 
for i in range(n):
    items = map(int,input().split())
    for j in items:
        if len(min_heap) < n:
            heapq.heappush(min_heap, j)
        else:
            if min_heap[0] < j:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, j)
 
print(min_heap[0])

