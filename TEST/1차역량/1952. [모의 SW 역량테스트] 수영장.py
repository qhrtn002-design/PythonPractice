def dfs(month,fee):
    global ans
    if month >=12:
        ans=min(fee,ans)
        return
    dfs(month+1,fee + lst[month]*day)
    dfs(month+1,fee + mon)
    dfs(month+3,fee + mon3)

t=int(input())
for s in range(t):
    day, mon, mon3, ans = map(int,input().split())
    lst = list(map(int,input().split()))
    dfs(0,0)
    print(f'#{s+1} {ans}')