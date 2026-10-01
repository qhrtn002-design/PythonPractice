from collections import deque

def bfs():
    q=deque()

    for i in range(1, len(cnt)):
        if cnt[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        print(node,end=' ')
        for next_node in lst[node]:
            cnt[next_node] -= 1

            if cnt[next_node] <= 0:
                q.append(next_node)


for tc in range(1, 11):
    v,e = map(int, input().split())
    info = list(map(int, input().split()))
    lst = [[] for _ in range(v+1)]
    cnt = [0] * (v+1)

    for i in range(0, e*2, 2):
        a,b = info[i], info[i+1]
        lst[a].append(b)
        cnt[b] += 1
    print(f'#{tc} ', end='')
    bfs()
    print()