num = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#전체 달 날짜, 월 수에 맞게 인덱스 조정을 위해 맨 앞 0추가
for i in range(1,num+1):
    a,b,c,d = map(int, input().split())
    ans1, ans2 = 0, 0 #초기 날짜 값 두개 설정 필수

    for x in range(a):
        ans1 += day[x] #첫 월직전의 달까지 날짜 합
    ans1 += b #해당 월의 날짜 더하기

    for y in range(c):
        ans2 += day[y]
    ans2 += d

    print(f'#{i} {ans2-ans1+1}')