t = int(input())

for s in range(1,t+1):
    n, m = map(int,input().split())
    print(f'#{s} {(n+m)%24}')