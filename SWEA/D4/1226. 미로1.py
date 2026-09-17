def dfs(x,y):
    global ans
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if arr[nx][ny] == '0' and not visited[nx][ny]:
            dfs(nx,ny)
        if arr[nx][ny] == '3':
            ans = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    ans = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                dfs(i,j)
    print(f'#{tc} {ans}')