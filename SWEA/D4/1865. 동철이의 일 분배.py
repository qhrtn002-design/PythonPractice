def dfs(worker, prob):
    global ans
    if worker == n:
        ans = max(ans,prob)
        return
    if prob <= ans:
        return

    for i in range(n):
        if arr[worker][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(worker+1,prob*arr[worker][i]/100)
            visited[i] = 0

t = int(input())
for s in range(t):
    n = int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans = 0
    visited = [0]*n

    dfs(0,100)
    print(f'#{s+1} {ans:.6f}')