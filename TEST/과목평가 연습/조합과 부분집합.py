def dfs(num,idx):
    if num == m:
        print(*ans)
        return
    
    for i in range(idx,n+1):
        ans.append(i)
        dfs(num+1,i+1)
        ans.pop()

t=int(input())
for tc in range(t):
    n,m = map(int,input().split())
    ans = []
    print(f'#{tc+1}')
    dfs(0,1)