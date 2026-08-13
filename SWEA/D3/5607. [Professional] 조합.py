t = int(input())
for s in range(t):
    n, r = map(int, input().split())
    r = min(r, n-r)
    num,d = 1,1
    for i in range(1,r+1):
        num = num*(n-r+i)%1234567891
        d = d*i%1234567891
    ans = num*pow(d,1234567891-2,1234567891)%1234567891
    print(f'#{s+1} {ans}')