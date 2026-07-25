t = int(input())
for s in range(1, t+1):
    n, m = map(int, input().split())
    if n > 9 or m > 9:
        ans = -1
    else:
        ans = n * m
    print(f'#{s} {ans}')