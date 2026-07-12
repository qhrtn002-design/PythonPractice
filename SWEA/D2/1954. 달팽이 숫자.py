a = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0] #dx dy 의 순서로 방향을 설정.
# dir을 이용해서 인덱스 카운팅.
# dx[dir] 와 dy[dir]로 (0,1) = 오른쪽 방향

for i in range(1,a+1):
    print(f'#{i}')

    n = int(input())
    arr = [[0]*n for k in range(n)] #n만큼 0으로 기초 배열 스케치

    x,y = 0, 0
    dir = 0
    for num in range(1, n*n+1): #1 부터 n*n까지 차례대로 배열에 출력
        arr[x][y] = num

        nx = x + dx[dir] # 다음칸 지정
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
        # 다음 칸에 값이 들어갈 수 있는 조건 3개.
        # nx가 범위 안인지, ny가 범위 안인지, 다음 칸에 값이 안들어갔는지.
            x = nx
            y = ny
        else:
            dir = (dir+1) % 4 # 방향에 1을 계속 더하지만, 나머지를 활용해서 인덱스로 활용
            # 방향이 4개이므로, 4에 대한 나머지 사용
            x += dx[dir] 
            y += dy[dir] # 칸이 꽉 차거나 범위 밖이면, 방향 전환

    for row in arr:
        print(*row) # 전체 배열 출력. 
        # 행단위로 출력 (*row). 해당 row의 모든 요소 출력

        