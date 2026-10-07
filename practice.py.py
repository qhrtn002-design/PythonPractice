# 우선 순위 큐

import heapq
arr = [3,234,23,12,31]
heap = []
for i in range(len(arr)):
    heapq.heappush(heap,-arr[i])

for i in range(len(arr)):
    print(-heapq.heappop(heap), end=' ')