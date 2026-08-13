t = int(input())
for s in range(t):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    dp = [0]*(k+1)
    dp[0] = 1
    for i in lst:
        for j in range(k,i-1,-1):
            dp[j] += dp[j-i]
    print(f'#{s+1} {dp[k]}')