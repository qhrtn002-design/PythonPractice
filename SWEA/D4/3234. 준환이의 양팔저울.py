from math import factorial

def dfs(cnt, left, right):
    global ans
    if left >= (total/2):
        ans += 2**(n-cnt) * factorial(n-cnt)
        return

    if cnt == n:
        ans += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(cnt+1, left+lst[i], right)
        if left>=right+lst[i]:
            dfs(cnt+1, left, right+lst[i])
        visited[i] = 0

t=int(input())
for s in range(t):
    n=int(input())
    lst = list(map(int, input().split()))
    ans = 0
    visited=[0]*n
    total = sum(lst)
    dfs(0,0,0)
    print(f'#{s+1} {ans}')