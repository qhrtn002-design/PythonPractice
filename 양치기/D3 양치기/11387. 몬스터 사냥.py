t = int(input())
for s in range(1,t+1):
    d,l,n = map(int, input().split())
    deal = 0
    for i in range(n):
        deal += d*(1+i*(l*(1/100)))
    print(f'#{s} {int(deal)}')