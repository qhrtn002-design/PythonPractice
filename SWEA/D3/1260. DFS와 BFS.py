from collections import deque
n, m, v = map(int, input().split())
#n : 노드개수 m: 간선개수 v:시작노드
node = [[] for _ in range(n+1)]
for s in range(m):
    a, b = map(int, input().split())
    #간선이 연결하는 두 노드
    node[a].append(b)
    node[b].append(a)

for i in range(1,n+1):
    node[i].sort()
stack = [v]
visited = [False] * (n+1)
while stack:
    now = stack.pop()
    if visited[now]:
        continue
    visited[now] =True
    print(now, end=' ')
    for i in reversed(node[now]):
        if not visited[i]:
            stack.append(i)
print()

queue = deque([v])
visited = [False] * (n+1)
while queue:
    now = queue.popleft()
    if visited[now]:
        continue
    visited[now] = True
    print(now, end = ' ')
    for i in node[now]:
        if not visited[i]:
            queue.append(i)
