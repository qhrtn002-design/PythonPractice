t = int(input())
for s in range(1,t+1):
    n = int(input())
    ans = 'Alice' if n%2==0 else 'Bob'
    print(f'#{s} {ans}')