def dfs(x,y):
    visited[x][y] = 1
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > day and not visited[nx][ny]:
            dfs(nx,ny)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

t=int(input())
for tc in range(t):
    n = int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    ans = 1
    for day in range(1,101):
        visited = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > day and not visited[i][j]:
                    dfs(i,j)
                    cnt += 1
        ans = max(ans,cnt)

    print(f'#{tc+1} {ans}')