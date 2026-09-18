from copy import deepcopy

T = int(input())

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def go_robot(r, c, dir):
    crop = 0
    temp_graph = deepcopy(graph)

    K = [[1]*N for _ in range(N)]
    for day in range(1, M+1):

        can_move = False
        for dir_dr in range(-1, 3):
            temp_dir = (dir+dir_dr)%4
            nr = r+dr[temp_dir]
            nc = c+dc[temp_dir]

            # 산 또는 수확 불가능 상태
            if temp_graph[nr][nc] == 1 or temp_graph[nr][nc] > day:
                continue

            # 이동 가능한 곳 발견
            can_move = True
            dir = temp_dir
            break

        # 오전
        if temp_graph[r][c] == 0:
            if not can_move:
                continue
            temp_graph[r][c] = day+(3+K[r][c])+1
            K[r][c] += 1
        else:
            temp_graph[r][c] = 0
            crop += 1
        
        # 오후
        if can_move:
            r, c = nr, nc

    return crop

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 0:
                for dir in range(4):
                    answer = max(answer, go_robot(r, c, dir))

    print(f'#{tc} {answer}')