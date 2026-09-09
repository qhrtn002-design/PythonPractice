t=int(input())
dx=[0,1,0,-1]
dy=[1,0,-1,0]
for s in range(t):
    n=int(input())
    arr=[list(map(int,input().split()))for _ in range(n)]
    ans=1
    for i in range(n):
        for j in range(n):
            x,y=i,j
            step=1
            while 1:
                minh = float('inf')
                ndir = -1
                for dir in range(4):
                    nx=x+dx[dir]
                    ny=y+dy[dir]

                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if arr[nx][ny] >=arr[x][y]:
                        continue

                    if minh>arr[nx][ny]:
                        minh = arr[nx][ny]
                        ndir = dir
                if ndir == -1:
                    break
                x=x+dx[ndir]
                y=y+dy[ndir]
                step+=1
            ans = max(ans,step)
    print(f'#{s+1} {ans}')