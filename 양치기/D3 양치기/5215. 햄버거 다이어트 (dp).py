t = int(input())
for s in range(t):
    n, l = map(int, input().split())
    dp=[0]*(l+1)
    for _ in range(n):
        score, cal = map(int, input().split())
        for i in range(l, cal-1, -1):
            dp[i] = max(dp[i], dp[i-cal]+score)
    print(f'#{s+1} {dp[l]}')