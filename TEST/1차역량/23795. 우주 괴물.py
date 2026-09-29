t=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for s in range(t):
    n = int(input())
    arr=[list(map(int, input().split()))for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x,y=i,j
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        while 0<=ny<n and 0<=nx<n:
            if arr[nx][ny] == 1:
                break
            if arr[nx][ny] == 0:
                arr[nx][ny] = 2
            nx+=dx[d]
            ny+=dy[d]
    ans=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                ans+=1
    print(f'#{s+1} {ans}')