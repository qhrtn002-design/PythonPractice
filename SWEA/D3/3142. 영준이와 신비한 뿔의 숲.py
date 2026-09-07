t = int(input())
for s in range(t):
    n,m=map(int, input().split())
    print(f'#{s+1} {2*m-n} {n-m}')