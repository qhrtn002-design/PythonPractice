t=int(input())
for s in range(t):
    n,m=map(int, input().split())
    arr=[input()for _ in range(n)]
    ans=float('inf')
    for w in range(n-2):
        for b in range(w+1,n-1):
            cnt=0
            for i in range(w+1):
                for j in range(m):
                    if arr[i][j] !='W':
                        cnt+=1
            for i in range(w+1, b+1):
                for j in range(m):
                    if arr[i][j] !='B':
                        cnt+=1
            for i in range(b+1,n+1):
                for j in range(m):
                    if arr[i][j] !='R':
                        cnt+=1
            ans = min(ans,cnt)
    print(f'#{s+1} {ans}')