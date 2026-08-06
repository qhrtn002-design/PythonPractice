n, m, v = map(int, input().split())
#n : 노드개수 m: 간선개수 v:시작노드
node = [[] for _ in range(n+1)]
for s in range(m):
    a, b = map(int, input().split())
    #간선이 연결하는 두 노드
    node[a].append(b)
    node[b].append(a)

stack = [v]
visited = [False] * (n+1)
while stack:
    now = stack.pop()
    if visited[now]:
        continue
    visited[now] =True
    print(now, end=' ')
    for i in node[now]:
        if not visited[i]:
            stack.append(i)