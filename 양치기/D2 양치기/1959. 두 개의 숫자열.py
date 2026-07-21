t = int(input())

for s in range(1,t+1):
    n,m = map(int, input().split())

    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))

    ans = 0
    
    if len(lsta) > len(lstb):
        for k in range(abs(n-m)+1):
            total = 0
            for i in range(m):
                total += lsta[i+k] * lstb[i]
            
            ans = max(ans, total)

    else:
        for k in range(abs(n-m)+1):
            total = 0
            for i in range(n):
                total += lsta[i] * lstb[i+k]
            ans = max(ans, total)
    print(f'#{s} {ans}')
            

