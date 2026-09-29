def dfs(x,y):
    global cnt #카운팅변수 글로벌로 호출
    cnt += 1 #시작하면서 한마리 추가
    visited[x][y] = 1 #방문했으므로 방문배열체크
    for d in range(4): # 4방향 탐색
        nx=x+dx[d]
        ny=y+dy[d]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == '1' and not visited[nx][ny]: #다음좌표가 범위 내, 아직 방문하지 않은 양이라면
            dfs(nx,ny) #재귀함수 호출

dx = [1,-1,0,0]
dy = [0,0,1,-1] #dx dy 설정

t=int(input()) #테스트케이스 횟수 입력받기
for s in range(t): #테스트케이스 횟수만큼 반복
    n=int(input()) #배열의 크기 입력받기
    arr = [input().split() for _ in range(n)] #배열 전체 입력
    visited = [[0]*n for _ in range(n)] #배열과 같은 크기의 방문배열 설정
    wolf = 0 #정답 초기값 설정
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '1' and not visited[i][j]: #배열을 반복해서 돌며, 아직 방문하지 않았다면 dfs 실행 조건
                cnt = 0 #양 떼들 마다 카운팅 초기화
                dfs(i,j)
                if cnt>=5: #만약 양 떼가 5마리 이상이면 늑대 한마리 추가
                    wolf += 1

    print(f'#{s+1} {wolf}')