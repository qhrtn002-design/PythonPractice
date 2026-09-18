def comb(num, idx):
    #num : 지금까지 고른 치킨 집 수, idx : 다음에 볼 치킨집
    global result
    if num == m: #치킨집을 정해진 m개 만큼 봤을 때,
        total = 0
        for hx, hy in home:
            min_dis=float('inf')
            for kx,ky in ans:
                dis = abs(hx-kx) + abs(hy-ky) # 각 집과 치킨집 간의 거리를 계산하고
                if min_dis > dis:
                    min_dis = dis
            total += min_dis # 그 집마다의 맨해튼 거리의 최소값을 total에 합친다.
        result = min(total, result) 
        # 그리고 모든 조합만큼 치킨집을 다 본 결과에 대한 최소값을 다시 result에 반영
        return
    for i in range(idx, len(chicken)): #치킨집을 idx 부터 고르기
        ans.append(chicken[i]) #치킨집 보기
        comb(num+1, i+1) #봤으니까 다음 치킨집으로 확인
        ans.pop() #다 봤으면 다음 치킨집으로 가기위해 자리비움

n,m = map(int,input().split()) #m개의 치킨집에 대한 최소거리 구하기
city=[list(input().split())for _ in range(n)]
result = float('inf')
home = [] # 발견한 집 좌표 목록
chicken = [] # 발견한 치킨집 좌표 목록
ans=[] #지금까지 선택한 치킨집 목록
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            home.append((i,j))
        elif city[i][j] == '2':
            chicken.append((i,j))
comb(0,0) #아직 아무런 치킨집도 보지 못했으므로 0부터 시작
print(result)