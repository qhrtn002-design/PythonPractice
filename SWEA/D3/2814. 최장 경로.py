def dfs(node, cnt):
    global ans
    visited[node] = 1
    ans = max(ans,cnt)

    for i in graph[node]:
        if not visited[i]:
            dfs(i,cnt+1)
    visited[node] = 0
    
t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    ans = 0
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1,n+1):
        dfs(i,1)

    print(f'#{s+1} {ans}')