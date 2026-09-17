from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs():
    global ans

    q = deque()
    visited = [[0]*m for _ in range(n)]
    #출발 준비
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                q.append((i,j))

    step = 1
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()

            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx>= n or ny<0 or ny>=m:
                    continue
                if visited[nx][ny] or arr[nx][ny] == 'W':
                    continue

                ans += step
                visited[nx][ny] = 1
                q.append((nx,ny))
        step+=1


t= int(input())
for s in range(t):
    ans = 0
    n, m = map(int, input().split())
    arr = [input()for _ in range(n)]
    bfs()

    print(f'#{s+1} {ans}')