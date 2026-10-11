def dfs(idx):
    global cnt
    if sum(ans) >= k:
        cnt += 1

    for i in range(idx,n):
        ans.append(lst[i])
        dfs(i+1)
        ans.pop()

t = int(input())
for tc in range(t):
    n,k = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = []
    cnt = 0
    print(f'#{tc+1}',end=' ')
    dfs(0)
    print(cnt)