t = int(input())

direction = [(0,1), (1,0), (0,-1), (-1,0)] 

for s in range(1,t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x, y, idx = 0, 0, 0
    for i in range(1, n*n+1):
        
            arr[x][y] = i
            dx, dy = direction[idx]
            nx = x + dx
            ny = y + dy

            if 0<=nx < n and 0<= ny < n and arr[nx][ny] == 0:
                x = nx
                y = ny
            else:
                idx = (idx+1)%4
                dx, dy = direction[idx]
                x += dx
                y += dy

    print(f'#{s}')
    for row in arr:
        print(*row)