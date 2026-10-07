import heapq

def prim():
    global answer

    pq = []
    visited = [0] * N
    distances = [float('inf')] * N

    visited[0] = 1

    for i in range(1, N):
        i_distance = (xs[0] - xs[i]) ** 2 + (ys[0] - ys[i]) ** 2
        distances[i] = i_distance
        heapq.heappush(pq, (i_distance, i))

    count = 0

    while count < N - 1:
        dis, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        answer += dis
        count += 1

        for i in range(N):
            if visited[i]:
                continue

            i_distance = (xs[node] - xs[i]) ** 2 + (ys[node] - ys[i]) ** 2

            if distances[i] <= i_distance:
                continue

            distances[i] = i_distance
            heapq.heappush(pq, (i_distance, i))


T = int(input())

for tc in range(1, T + 1):
    answer = 0

    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    prim()

    answer = round(answer * E)

    print(f'#{tc} {answer}')