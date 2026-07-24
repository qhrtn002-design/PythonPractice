t = int(input())
for s in range(1,t+1):
    n,m = map(int,input().split())
    total = 0
    for i in range(n):
        total += 2**i
    ans = 'ON' if m & total == total else 'OFF'

    print(f'#{s} {ans}')
