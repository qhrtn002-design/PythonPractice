t = int(input())
for s in range(t):
    n = int(input())
    ans = list(map(int, input().split()))
    print(f'#{s+1} {max(ans)-min(ans)}')