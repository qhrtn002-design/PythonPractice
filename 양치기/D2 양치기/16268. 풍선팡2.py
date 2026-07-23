t = int(input())

cross = [(0,1),(1,0),(0,-1),(-1,0)]

for s in range(1,t+1):
    n,m = map(int, input().split())
    arr = [(list(map(int,input().split())))for _ in range(n)]

    ans = 0
    
    for i in range(n):
        for j in range(m):
            total = 0
            total += arr[i][j]

            for dx, dy in cross:
                nx = i + dx
                ny = j + dy

                if 0<=nx<=n-1 and 0<=ny<=m-1:
                    total += arr[nx][ny]

            ans = max(ans,total)
            
    print(f'#{s} {ans}')