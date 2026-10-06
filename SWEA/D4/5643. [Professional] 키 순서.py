from collections import deque

def bfs(start,graph):
    q = deque()
    visited = [0]*(n+1)
    q.append(start)
    visited[start] = 1
    cnt = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt
    
t=int(input())
for tc in range(t):
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    reverse = [[] for _ in range(n+1)]
    ans = 0
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        reverse[b].append(a)

    for i in range(1,n+1):
        big = bfs(i,graph)
        small = bfs(i,reverse)
        if big + small == n-1:
            ans += 1
    print(f'#{tc+1} {ans}')