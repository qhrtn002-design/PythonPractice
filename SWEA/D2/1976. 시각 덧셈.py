n = int(input())
hour = 0
minute = 0 #시간, 분 지정

for i in range(1,n+1):
    a,b, c,d = map(int, input().split()) #2개의 시간 받기
    hour = (a+c) % 12 
    minute = (b+d) % 60 #시간 계산 및 분계산 
    if minute >= 1: 
        hour += (b+d) // 60 #분이 60 넘을 때, 시간으로 더해서 계산
        print(f'#{i} {hour} {minute}')