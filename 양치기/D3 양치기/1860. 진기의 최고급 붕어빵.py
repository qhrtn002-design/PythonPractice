t = int(input())
for s in range(1,t+1):
    people_num,make_time,bread_num = map(int, input().split())
    visit_time = list(map(int, input().split()))
    visit_time.sort()
    ans = 'Possible'
    for i in range(people_num):
        if (visit_time[i]//make_time) * bread_num < i + 1:
            # visit_time[i]//make_time = 손님이 도착할 때까지 만드는 횟수
            # 거기에 개수를 곱하면 손님 도착시점에 있는 붕어빵 개수
            # i+1 : 지금까지 방문한 손님 수. 0부터 시작하므로 1더함
            ans = 'Impossible'
            break       
    print(f'#{s} {ans}') 