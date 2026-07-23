t = int(input())
cross = [(0,1), (1, 0), (0, -1), (-1, 0)]

for s in range(1,t+1):
    n,m = map(int, input().split())
    arr = [(list(map(int,input().split())))for _ in range(n)]

    ans = 0
    
    for i in range(n):
        for j in range(m):
            
            
    print(f'#{s} {ans}')