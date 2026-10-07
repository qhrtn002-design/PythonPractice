import heapq
dx = [1,-1,0,0]
dy = [0,0,1,-1]

t=int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int,input().strip())) for _ in range(n)]
    pq= []
    dis = [[float('inf')] * n for _ in range(n)]
    # 칸 마다 발생되는 최소 누적 비용을 저장하는 배열
    dis[0][0] = 0 # 첫 출발점 선언

    heapq.heappush(pq,(0,0,0)) # 출발점 heap에 기록
    while pq: # 힙이 빌 때까지 반복
        cost,x,y = heapq.heappop(pq) # 힙에 넣은 걸 순서대로 비용, x좌표, y좌표 명시
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n:
                new_cost = cost + arr[nx][ny] #new_cost 에 누적 비용 명시
                if new_cost < dis[nx][ny]:
                    # 만약 누적 비용이 앞으로 갈 비용보다 작으면
                    dis[nx][ny] = new_cost # 다음 비용 갱신
                    heapq.heappush(pq,(new_cost,nx,ny))
                    # 반복해서 새로운 비용과 다음 값 주소를 힙에 저장
    ans = dis[n-1][n-1] # 도착점 직전까지 비용

    print(f'#{tc+1} {ans}')