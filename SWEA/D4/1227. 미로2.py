from collections import deque

def bfs(x,y):
    global ans
    q=deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0<=nx<100 and 0<=ny<100):
                continue
            if not visited[nx][ny] and arr[nx][ny] == '0':
                q.append((nx,ny))
                visited[nx][ny] = 1
            if arr[nx][ny] == '2':
                ans = 1
                return

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(10):
    n = int(input())
    arr = [input() for _ in range(100)]
    ans = 0
    visited = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == '3':
                bfs(i,j)
    print(f'#{n} {ans}')