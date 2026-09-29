t=int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dig1=[1,1,-1,-1]
dig2=[1,-1,1,-1]
for s in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            x,y=i,j
            cross,dig=arr[x][y],arr[x][y]
            for k in range(4):
                for p in range(1,m):
                    nx=x+dx[k]*p
                    ny=y+dy[k]*p
                    if nx<0 or ny<0 or nx>=n or ny>=n:
                        continue
                    cross+=arr[nx][ny]

            for k in range(4):
                for p in range(1,m):
                    nx=x+dig1[k]*p
                    ny=y+dig2[k]*p
                    if nx<0 or ny<0 or nx>=n or ny>=n:
                        continue
                    dig+=arr[nx][ny]
            ans=max(ans,cross,dig)

    print(f'#{s+1} {ans}')
