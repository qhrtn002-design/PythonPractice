def dfs(x,y): # 받은 좌표를 토대로 진입
    global cnt
    visited[x][y] = 1 # 일단 도착지점엔 왔다고 표시하고
    cnt+=1 # 1의 개수를 카운트
    for d in range(4): # 방향 4개를 반복하면서 
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 1 and not visited[nx][ny]:
            # 다음 좌표가 범위 안이고, 다음칸이 1이며, 아직 방문하지 않은 1이라면,
            dfs(nx,ny) #재귀함수를 통해 이동하며, 거기서 다시 카운트 수행

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] #크기가 똑같은 방문배열
dx=[1,-1,0,0]
dy=[0,0,1,-1]
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]: #단지가 있고, 아직 방문하지 않았다면,
            cnt = 0 #카운트를 생성하고(초기화)
            dfs(i,j) #dfs 실행
            ans.append(cnt) #단지의 집 개수를 리스트에 넣음
ans.sort()
print(len(ans))
for i in ans:
    print(i)