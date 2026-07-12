num = int(input())

for i in range(1, num+1):
    a, b, c, d = map(int, input().split())
    #처음 시간, 분 입력 받기

    hour = (a+c)%12 #시간 계산 12시간단위로
    minute = (b+d)%60 #분 계산 60분 단위로

    if b+d >= 60: # 분 합계가 60분 초과시 시간 추가
        hour +=1

        
    print(f'#{i} {hour} {minute}')