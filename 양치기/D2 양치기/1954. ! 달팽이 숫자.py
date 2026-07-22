t = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for s in range(1,t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x, y, dir = 0, 0, 0
    for i in range(1, n*n+1):
        arr[x][y] = i

        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0<=nx < n and 0<= ny < n and arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            dir = (dir+1)%4
            x += dx[dir]
            y += dy[dir]

    print(f'#{s}')
    for u in arr:
        print(*u)