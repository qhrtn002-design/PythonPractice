def check_plus(r, c, visited):
    for i in range(N):
        if visited & (1<<i):
            continue

        if abs(r-home_info[i][0])+abs(c-home_info[i][1]) <= home_info[i][2]:
            visited |= (1<<i)
    
    return visited
        
def calc_dis():
    total_distance = 0

    for home_idx in range(N):
        distance = float('inf')
        for charge_r, charge_c in pick_rcs:
            distance = min(distance, abs(charge_r-home_info[home_idx][0])+abs(charge_c-home_info[home_idx][1]))
        total_distance += distance

    return total_distance

def pick_charge(count, idx):
    global distances, visited

    # 다 충전 가능하면 끝
    if visited == (1<<N)-1:
        distances[count-1] = min(distances[count-1], calc_dis())
        return

    # 2개 다 골라봤으면 끝 or 1개로 다 충전 가능하면, 2개째 고를 필요 없음
    if count == 2 or (count == 1 and distances[0] < float('inf')):
        return

    for i in range(idx, 31*31):
        if i in not_i:
            continue

        r = i // 31
        c = i % 31
        i_visited = check_plus(r, c, visited)

        if i_visited != visited:
            backup = visited
            visited = i_visited    
            pick_rcs.append((r, c))
            pick_charge(count+1, i+1)
            visited = backup
            pick_rcs.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    home_info = []
    not_i = set()
    for _ in range(N):
        r, c, coverage = map(int, input().split())
        r += 15
        c += 15
        not_i.add(r*31+c)
        home_info.append((r, c, coverage))
        
    distances = [float('inf'), float('inf')]
    visited = 0

    # count, idx
    pick_rcs = []
    pick_charge(0, 0)

    answer = -1
    if distances[0] != float('inf'):
        answer = distances[0]
    elif distances[1] != float('inf'):
        answer = distances[1]

    print(f'#{tc} {answer}')