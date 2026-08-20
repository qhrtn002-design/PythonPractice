t=int(input())
for s in range(t):
    a,b=map(int, input().split())
    print(f'#{s+1} {(a//b)**2}')