from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        now = q.popleft()
        
        if now == m:
            return visited[now] - 1
        next_node = [now+1,now-1,now*2,now-10]
        
        for i in next_node:
            if 1<=i<=1000000 and not visited[i]:
                q.append(i)
                visited[i] = visited[now] + 1

t=int(input())
for tc in range(t):
    n,m=map(int,input().split())
    visited = [0] * 1000001
    ans = bfs(n)

    print(f'#{tc+1} {ans}')