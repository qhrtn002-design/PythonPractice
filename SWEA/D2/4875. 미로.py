def dfs(x,y):
    global ans
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and arr[nx][ny] == '0':
                dfs(nx,ny)
            elif arr[nx][ny] == '3':
                ans = 1
t=int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for s in range(t):
    n=int(input())
    arr=[list(input()) for _ in range(n)]
    visited=[[0]*n for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                dfs(i,j)
    print(f'#{s+1} {ans}')