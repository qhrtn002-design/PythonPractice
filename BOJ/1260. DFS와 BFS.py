from collections import deque
n, m, v = map(int, input().split())
# n: 노드 개수 / m: 간선 개수 / v: 시작 노드
node = [[] for _ in range(n+1)]
# 인접 리스트 생성, n+1인 이유는 노드가 1번부터 시작하기 때문
for s in range(m):
    a, b = map(int, input().split())
    # 연결된 두 노드 입력
    node[a].append(b)
    node[b].append(a)
    # 무방향 그래프이므로 양쪽에 서로를 넣음
for i in range(1,n+1):
    node[i].sort()
    # 작은 번호부터 방문하기 위해 정렬

stack = [v]
# DFS: 시작 노드를 스택에 넣음
visited = [False] * (n+1)
# 방문 여부 저장
while stack:
    now = stack.pop()
    # 스택의 마지막 값을 꺼냄 → LIFO
    if visited[now]:
        continue
    # 이미 방문했으면 넘어감
    visited[now] = True
    # 방문 처리
    print(now, end=' ')
    for i in reversed(node[now]):
        # 스택은 뒤에서 꺼내므로 작은 번호가 먼저 나오도록 역순으로 넣음
        if not visited[i]:
            stack.append(i)
            # 다음에 방문할 노드를 스택에 넣음
print()

queue = deque([v])
# BFS: 시작 노드를 큐에 넣음
visited = [False] * (n+1)
# DFS와 별도로 방문 기록 초기화
while queue:
    now = queue.popleft()
    # 큐의 앞에서 꺼냄 → FIFO
    if visited[now]:
        continue
    # 이미 방문했으면 넘어감
    visited[now] = True
    # 방문 처리
    print(now, end=' ')
    for i in node[now]:
        # 연결된 노드를 작은 번호부터 확인
        if not visited[i]:
            queue.append(i)
            # 다음에 방문할 노드를 큐에 넣음