
T = int(input()) #처음 주어진 숫자 받기

for tc in range(1, T + 1): #숫자만큼 반복
    date = input() # 이제 받은 숫자만큼 날짜 받기

    y = date[:4] #여긴 왜 int를 안쓰지? > 맨앞에 0 사라짐 방지
    m = int(date[4:6])
    d = int(date[6:8])

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= m <= 12 and 1 <= d <= days[m - 1]:
        print("#{} {}/{:02d}/{:02d}".format(tc, y, m, d)) #형식에 맞게 출력
    else:
        print("#{} -1".format(tc))