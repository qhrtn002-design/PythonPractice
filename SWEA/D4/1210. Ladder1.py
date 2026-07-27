for s in range(10):
    t = int(input())
    arr = [list(map(int,input().split()))for _ in range(100)]
    x,y = 0,0
    for k in range(100):
        if arr[99][k] == 2:
            x = 99
            y = k
    start = (x,y)

    while x!=0:
        arr[x][y] = 0
        if y>0 and arr[x][y-1] == 1:
            y -= 1
        elif y<99 and arr[x][y+1] == 1:
            y += 1
        else:
            x -= 1
    
    print(f'#{t} {y}')
