a = int(input())

for s in range(1,a+1):
    n, m = map(int, input().split())

    arr = [] #초기 배열 지정
    kill = 0 #테스트 케이스 마다 최댓값 초기화

    for i in range(n):
        ans = list(map(int, input().split()))
        arr.append(ans) #줄 반복해서 더하면서 파리 배열 생성

    ps = [[0]* n for _ in range(n)] #누적합 배열 생성
    for a in range(n):
        for b in range(n):
            if a == 0 and b == 0:
                ps[0][0] = arr[0][0] #첫 칸 더하기
            elif a == 0:
                ps[0][b] = ps[0][b-1]+arr[0][b] #맨 윗줄 누적합 더하기
            elif b == 0:
                ps[a][0] = ps[a-1][0] + arr[a][0] #맨 왼쪽 줄 누적합 더하기
            else: #위쪽 + 왼쪽 - 중복지역 + 현재값
                ps[a][b] = ps[a-1][b] + ps[a][b-1] -ps[a-1][b-1] + arr[a][b]

    
    for q in range(n-m+1): #파리채 반복 이동
        for p in range(n-m+1):
            total = 0

            total = ps[q+m-1][p+m-1] #파리채 범위 오른쪽 하단 누적합 가져오기
            if q>0:
                total -= ps[q-1][p+m-1] #q가 1이상일때, 위쪽 누적합 빼기
            if p>0:
                total -= ps[q+m-1][p-1] #p가 1이상일때, 왼쪽 누적합 빼기
            if q>0 and p>0:
                total += ps[q-1][p-1] #겹친 곳 두번 빠졌으니 한번 더하기

            if total > kill:
                kill = total

    print(f'#{s} {kill}')