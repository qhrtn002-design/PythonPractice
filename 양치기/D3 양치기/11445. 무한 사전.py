t = int(input())
for s in range(1,t+1):
    p = input().strip()
    q = input().strip()
    ans = 'Y'
    if q == p + 'a':
        ans = 'N'
    print(f'#{s} {ans}')