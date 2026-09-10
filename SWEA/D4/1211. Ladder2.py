for s in range(10):
    tc=int(input())
    arr=[list(map(int,input().split()))for _ in range(100)]
    ans=float('inf')
    result=0
    start=[]
    for y in range(100):
        if arr[0][y] == 1:
            start.append(y)

    for sy in start:
        x=0
        y=sy
        step=0
        visited=[[0]*100 for _ in range(100)]
        while x!=99:
            if y>0 and arr[x][y-1] == 1 and visited[x][y-1] == 0:
                y-=1
                step+=1
                visited[x][y] = 1
            elif y<99 and arr[x][y+1] == 1 and visited[x][y+1] == 0:
                y+=1
                step+=1
                visited[x][y] = 1            
            else:
                x+=1
                step+=1
                visited[x][y] = 1
        if step<ans:
            ans=step
            result=sy

    print(f'#{tc} {result}')