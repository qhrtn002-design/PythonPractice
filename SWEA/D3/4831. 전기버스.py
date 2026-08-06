t = int(input())
for s in range(t):
    k,n,m = map(int, input().split())
    charge = list(map(int,input().split()))
    bus, chargecnt = 0, 0
    while bus + k < n:
        for i in range(bus+k, bus, -1):
            if i in charge:
                bus = i
                chargecnt += 1
                flag = 1
                break
        else:
            chargecnt = 0
            break
    print(f'#{s+1} {chargecnt}')