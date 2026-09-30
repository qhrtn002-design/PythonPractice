t=int(input())
for s in range(t):
    day, mon, mon3, ans = map(int,input().split())
    lst = list(map(int,input().split()))

    dp = [0]*12
    for i in range(12):
        fees = [day*lst[i], mon, float('inf')]
        # 일권 사용 시, 월권 사용 시, 3개월 권 사용시

        if i > 0:
            fees[0] += dp[i-1]
            fees[1] += dp[i-1]
        # 첫 달 아닐때만 이전 달에 대해 누적 처리
    
        if i >= 2:
            fees[2] += mon3
            if i >= 3:
                fees[2] += dp[i-3]

        dp[i] = min(fees)

    ans = min(ans, dp[11])

    print(f'#{s+1} {ans}')