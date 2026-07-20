t = int(input())

for s in range(1,t+1):
    days = int(input()) #거래가능 날 수
    sell = list(map(int, input().split())) # 싯가 리스트

    topprice = 0 #최고가 설정
    money = 0 #이익 설정

    for price in sell[::-1]: #마지막 날 부터 판매가 반복
        if price > topprice: #최고가 설정 조건
            topprice = price #최고가 지정
        else:
            money += topprice - price #아닌 경우 최고가에서 가격 뺀게 이득이 됨
            

    print(f'#{s} {money}')