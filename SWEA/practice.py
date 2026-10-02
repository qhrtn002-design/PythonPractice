from collections import deque

def bfs():
    q= deque()
    q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                dis[i] = dis[now] + 1

t=int(input())
for tc in range(t):
    v,e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    dis = [0]*(v+1)
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s,g = map(int, input().split())
    bfs()
    print(f'#{tc+1} {dis[g]}')