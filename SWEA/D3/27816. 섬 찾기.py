def dfs(x,y):
    visited[x][y] = 1
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 'L' and not visited[nx][ny]:
            dfs(nx,ny)
        
dx=[1,-1,0,0]
dy=[0,0,1,-1]

t=int(input())
for s in range(t):
    n,m = map(int, input().split())
    arr=[list(input()) for _ in range(n)]
    visited=[[0]*m for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'L' and not visited[i][j]:
                dfs(i,j)
                ans+=1

    print(f'#{s+1} {ans}')