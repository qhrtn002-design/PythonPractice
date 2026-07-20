t = int(input())
week = { 'MON' :1,'TUE' :2,'WED' :3,'THU':4,'FRI' :5,'SAT' :6,'SUN' :7} #요일을 숫자로 받기
for i in range(1,t+1):
    day = input() #날짜 입력받기

    if day == 'SUN': #일요일 입력 받을 경우
        ans = 7 #다음 일요일까지 일주일
    else:
        ans = 7 - week[day] #나머진 인덱스 호출로 그냥 빼기

    print(f'#{i} {ans}')