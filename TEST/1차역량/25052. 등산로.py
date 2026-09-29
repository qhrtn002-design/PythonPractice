t= int(input())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for s in range(t):
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            x,y=i,j
            cnt=0
            while 1:
                minh=float('inf')
                ndir=-1
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if arr[nx][ny] < arr[x][y]:
                        if minh>arr[nx][ny]:
                            minh=arr[nx][ny]
                            ndir=k
                cnt+=1
                if ndir==-1:
                    break
                x+=dx[ndir]
                y+=dy[ndir]
            ans=max(ans,cnt)
    print(f'#{s+1} {ans}')