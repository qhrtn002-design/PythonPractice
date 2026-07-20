t = int(input())

for s in range(1, t+1):
    n, m = map(int, input().split())

    lst_a = list(map(int, input().split())) #리스트 받기
    lst_b = list(map(int, input().split())) #리스트 받기

    maxans = 0 #합계 최댓값
    for ct in range(abs(n-m)+1): #리스트 간격으로 반복횟수 잡기
        total = 0 #순간 3개 곱의 합계
        for x in range(min(n,m)): #두 리스트 중 짧은 길이만큼만 반복
            if n > m: #리스트 중 하나가 길면,
                total += lst_a[x+ct] * lst_b[x]
                #긴 쪽의 리스트가 하나씩 움직이며 다시 대조
            else:
                total += lst_a[x] * lst_b[x+ct]
        
        if total > maxans: #3개 곱의 합이 최댓값보다 크면
            maxans = total #최댓값 바꾸기

    print(f'#{s} {maxans}')