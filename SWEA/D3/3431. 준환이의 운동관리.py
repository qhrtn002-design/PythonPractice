t = int(input())
for s in range(1, t+1):
    l, u, x = map(int, input().split())
    gap = l - x
    if x > u:
        ans = -1
    elif x > l:
        ans = 0
    else:
        ans = gap
    print(f'#{s} {ans}')