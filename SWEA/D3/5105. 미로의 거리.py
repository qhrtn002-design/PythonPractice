def dfs(x,y,cnt):
    global ans
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if arr[nx][ny]=='0':
                dfs(nx,ny,cnt+1)
            if arr[nx][ny]=='3':
                ans = cnt
dx=[1,-1,0,0]
dy=[0,0,1,-1]
t=int(input())
for s in range(t):
    n=int(input())
    arr=[list(input()) for _ in range(n)]
    ans = 0
    visited=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                cnt = 0
                dfs(i,j,cnt)
    print(f'#{s+1} {ans}')