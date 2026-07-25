t = int(input())
for s in range(1,t+1):
    n = int(input())
    ans = 'Odd' if n%2 == 1 else 'Even'
    print(f'#{s} {ans}')