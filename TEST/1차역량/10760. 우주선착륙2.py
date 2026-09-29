t=int(input())
dx=[1,-1,0,0,1,-1,1,-1]
dy=[0,0,1,-1,1,-1,-1,1]
for s in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split()))for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            x,y=i,j
            cnt=0
            for d in range(8):
                nx=x+dx[d]
                ny=y+dy[d]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if arr[nx][ny] < arr[x][y]:
                    cnt+=1
            if cnt>=4:
                ans+=1
    print(f'#{s+1} {ans}')