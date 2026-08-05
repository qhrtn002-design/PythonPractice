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
    print(tankpoint)

    for m in move:
        for k in range(4):
            if m == cmd[k]:
                arr[tankpoint[0]][tankpoint[1]] = '.'
                nx = tankpoint[0] + dx[k]
                ny = tankpoint[1] + dy[k]                
                if 0 <= nx <h and 0 <= ny < w and arr[nx][ny] == '.':
                    arr[nx][ny] = tank[k]
                else:
                    arr[tankpoint[0]][tankpoint[1]] = tank[k]

            else: #인덱스 k 를 써야되는데 못쓰고 있다
                bx = tankpoint[0] + dx[k]
                by = tankpoint[1] + dy[k]
                if 0 <= bx < h and 0 <= by < w and arr[bx][by] == '.' or arr[bx][by] == '-':
                    if arr[bx][by] == '*':
                        arr[bx][by] = '.'
            
    print(f'#{s+1}',end='')
    for row in arr:
        print(*row)
# 문자	의미
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)