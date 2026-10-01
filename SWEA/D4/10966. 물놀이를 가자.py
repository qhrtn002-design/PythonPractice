from collections import deque

def bfs():
    global ans
    q = deque()
    visited = [[0]*m for _ in range(n)]
    step = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i,j))
                visited[i][j] = 1

    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny] == 'L':
                    ans += step
                    q.append((nx,ny))
                    visited[nx][ny] = 1
        step+=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

t=int(input())
for s in range(t):
    n,m = map(int, input().split())
    arr=[input() for _ in range(n)]
    ans = 0
    bfs()

    print(f'#{s+1} {ans}')