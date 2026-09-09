def dfs(cnt):
    visited[cnt] = 1
    for idx in graph[cnt]:
        if not visited[idx]:
            dfs(idx)
for s in range(10):
    visited=[0]*100
    tc, n = map(int,input().split())
    lst=list(map(int,input().split()))
    graph=[[]for _ in range(100)]
    for i in range(0, n*2, 2):
        a=lst[i]
        b=lst[i+1]
        graph[a].append(b)
    dfs(0)
    ans=visited[99]
    print(f'#{tc} {ans}')