t=int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for s in range(t):
    n=int(input())
    arr = [list(map(int,input().split()))for _ in range(n)]
    min_val = float('inf')
    max_val = float('-inf')
    for i in range(n):
        for j in range(n):
            x,y=i,j
            cnt=arr[x][y]
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                while 0<=nx<n and 0<=ny<n:
                    cnt += arr[nx][ny]
                    nx+=dx[k]
                    ny+=dy[k]
            max_val= max(cnt,max_val)
            min_val= min(cnt,min_val)
    print(f'#{s+1} {max_val-min_val}')