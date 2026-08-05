dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cmd = ['U', 'R', 'D', 'L']
tank = ['^','>','v','<']
t = int(input())
for s in range(t):
    h, w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    n = int(input())
    move = input()
    tankpoint = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] in tank:
                tankpoint.append(i)
                tankpoint.append(j)
    
    for m in move:
        if m in cmd:
            k = cmd.index(m)
            arr[tankpoint[0]][tankpoint[1]] = '.'
            nx = tankpoint[0] + dx[k]
            ny = tankpoint[1] + dy[k]                
            if 0 <= nx <h and 0 <= ny < w and arr[nx][ny] == '.':
                arr[nx][ny] = tank[k]
                tankpoint[0] = nx 
                tankpoint[1] = ny 
            else:
                arr[tankpoint[0]][tankpoint[1]] = tank[k]

        else:
            if arr[tankpoint[0]][tankpoint[1]] in tank:
                p = tank.index(arr[tankpoint[0]][tankpoint[1]])
                boltx = tankpoint[0] + dx[p]
                bolty = tankpoint[1] + dy[p]
                while 0<=boltx < h and 0<=bolty < w:
                    if arr[boltx][bolty] == '-' or arr[boltx][bolty] == '.':
                        boltx += dx[p]
                        bolty += dy[p]
                    elif arr[boltx][bolty] == '*':
                        arr[boltx][bolty] = '.'
                        break
                    elif arr[boltx][bolty] == '#':
                        break
             
    print(f'#{s+1} ',end='')
    for row in arr:
        print(''.join(row))
