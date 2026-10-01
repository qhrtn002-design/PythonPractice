from collections import deque

def bfs(x,y):
    global ans
    q = deque()
    visited[x][y] = 1
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0<=nx<n and 0<=ny<n):
                continue

            if not visited[nx][ny] and arr[nx][ny] == '0':
                q.append((nx,ny))
                visited[nx][ny] = 1

            if arr[nx][ny] == '2':
                ans = 1
                return

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
            if arr[i][j] == '3':
                bfs(i,j)
    print(f'#{s+1} {ans}')