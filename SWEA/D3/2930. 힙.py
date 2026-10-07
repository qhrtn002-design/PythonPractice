import heapq

t=int(input())
for tc in range(t):
    n = int(input())
    heap=[]
    ans = []
    for _ in range(n):
        data = list(map(int,input().split()))

        if data[0] == 1:
            heapq.heappush(heap,-data[1])
        else:
            if heap:
                ans.append(-heapq.heappop(heap))
            else:
                ans.append(-1)

    print(f'#{tc+1}',*ans)