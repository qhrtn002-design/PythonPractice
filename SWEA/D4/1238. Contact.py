from collections import deque

def bfs(node):
    global ans
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        ans = 0
        for _ in range(len(q)):
            now = q.popleft()

            for i in graph[now]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
            ans = max(ans, now)


for tc in range(10):
    n,start = map(int,input().split())
    lst = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    visited = [0] * (101)
    for i in range(0,n,2):
        graph[lst[i]].append(lst[i+1])        

    bfs(start)
    print(f'#{tc+1} {ans}')