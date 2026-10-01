from collections import deque

def bfs(x,y):
    global ans
    q=deque()
    q.append((x,y))
    visited[x][y] = 1
    step = 0
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not(0<=nx<n and 0<=ny<n):
                    continue

                if arr[nx][ny] == '0' and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

                if arr[nx][ny] == '2':
                    ans = step
                    return
        step+=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]

t=int(input())
for s in range(t):
    n = int(input())
    arr=[input() for _ in range(n)]
    ans = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '3':
                bfs(i,j)

    print(f'#{s+1} {ans}')