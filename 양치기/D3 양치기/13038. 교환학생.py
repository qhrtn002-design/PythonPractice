t = int(input())
for s in range(1,t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = float('inf')      #정답 초기값 무한대로 지정
    for i in range(7):      #일주일 만큼 반복
        cnt = 0             #지금까지 수업 들은 횟수
        day = 0             #수업 듣기 시작한 뒤 며칠됐는지?
        while cnt != n:     #목표 수업 횟수 채울 때까지 반복
            if lst[(i+day)%7] == 1: #수업이 있는 요일이면
                cnt += 1            # 카운트 1
            day += 1                #날짜도 하나 추가
        ans = min(day,ans)          #날짜와 무한대 중 최소값 구하기
    print(f'#{s} {ans}')