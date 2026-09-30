from collections import defaultdict
from math import factorial

def dfs(cnt, left, right):

    if dp[visited][left] > 0:
        return dp[visited][left]

    if left>=(total/2):
        dp[visited][left] = 2**(n-cnt) * factorial(n-cnt)
        return

    if cnt == n:
        return 1

    case_cnt = 0

    for i in range(n):
        if visited & (1 << i):
            continue
        visited |= (1 << i)
        
        dfs(cnt+1, left+lst[i], right)

        if left >= right+lst[i]:
            case_cnt += dfs(cnt+1, left, right+lst[i])
        visited ^= (1 << i)

    dp[visited][left] = case_cnt
    return dp[visited][left]

t=int(input())
for s in range(t):
    n=int(input())
    lst = list(map(int, input().split()))
    total = sum(lst)

    dp = [defaultdict(int) for _ in range(1<<n)]

    visited = 0
    ans = dfs(0,0,0)

    print(f'#{s+1} {ans}')