t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    print(f'#{s+1} {ans}')