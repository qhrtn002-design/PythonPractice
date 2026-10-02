def dfs(cnt):
    global ans
    if cnt == n:
        ans+=1
        return
    for c in range(n):
        if c in visited:
            continue

        for r in range(cnt):
            if cnt-r == abs(c-col[r]):
                break
        else:
            col[cnt] = c
            visited.add(c)
            dfs(cnt+1)
            visited.remove(c)

t=int(input())
for s in range(t):
    ans = 0
    n=int(input())
    col = [-1]*n
    visited=set()

    dfs(0)
    print(f'#{s+1} {ans}')