def dfs(x,y):
    global cnt
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if  0<=nx<n and 0<=ny<n and arr[nx][ny] == arr[x][y] + 1:
            cnt += 1
            dfs(nx,ny)

t=int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for s in range(t):
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_dis = 0 # 최대 거리 변수 지정
    for i in range(n):
        for j in range(n):
            cnt=1 # 테스트 케이스 보고 1로 시작하는지 판단가능
            start = arr[i][j] # 시작하는 방의 크기 지정
            dfs(i,j)

            if max_dis < cnt: # 측정한 거리가 최대거리보다 크다면
                max_dis = cnt # 최대거리는 갱신됨
                fir_start = start # 이 시점의 시작 방 크기값을 재설정

            elif cnt == max_dis: # 거리가 동점인 경우에는
                if fir_start > start: # 기존 시작 방번호가 지금 측정한 방보다 크면
                    fir_start = start # 지금의 더 작은 방으로 갱신됨 (크기가 작은 방크기로 지정)

    print(f'#{s+1} {fir_start} {max_dis}')