def spray(x, y, idx):
    total = arr[x][y]
    for dx, dy in idx:
        for k in range(1,m):
            nx = x + dx * k
            ny = y + dy * k

            if 0<=nx<n and 0<=ny<n:
                total += arr[nx][ny]
    return total

t = int(input())
cross=[(0,1), (1,0), (0,-1), (-1,0)]
dig=[(1,1), (1,-1), (-1,1), (-1,-1)]

for s in range(1,t+1):
    n,m = map(int,input().split())
    arr = [(list(map(int,input().split())))for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, spray(i,j,cross), spray(i,j,dig))

    print(f'#{s} {ans}')