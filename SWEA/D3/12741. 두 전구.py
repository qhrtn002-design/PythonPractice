t=int(input())
for s in range(t):
    a,b,c,d = map(int, input().split())
    ans = abs(c-b) if c <= b else 0
    print(f'#{s+1} {ans}')