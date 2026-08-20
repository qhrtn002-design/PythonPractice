t=int(input())
for s in range(t):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(f'#{s+1} {lst[m%n]}')