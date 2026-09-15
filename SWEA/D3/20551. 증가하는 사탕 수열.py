t=int(input())
for s in range(t):
    a,b,c=map(int, input().split())
    ans = 0
    if a<1 or b<2 or c<3:
        ans = -1
    else:
        if b>=c:
            ans += b-(c-1)
            b=c-1
        if a>=b:
            ans += a-(b-1)
            a=b-1
    print(f'#{s+1} {ans}')