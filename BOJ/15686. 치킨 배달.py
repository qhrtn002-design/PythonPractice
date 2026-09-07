def comb(num, idx):
    if num == m:
        return
    for i in range(idx, len(chicken)):
        ans.append(chicken[i])
        comb(num+1, i+1)
        ans.pop()

n,m = map(int,input().split())
city=[list(input().split())for _ in range(n)]

home = []
chicken = []
dis = 0
ans=[]
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            home.append((i,j))
        elif city[i][j] == '2':
            chicken.append((i,j))
