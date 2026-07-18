t = int(input())
money = [50000,10000,5000,1000,500,100,50,10] #주어진 화폐 리스트

for i in range(1,t+1):
    price = int(input()) #가격 받기
    pay = [] #출력할 화폐 개수 리스트

    for x in money:
        change = price//x #화폐를 몇개 쓸 수 있는지 저장
        if change > 0:
            pay.append(change) #현재 화폐의 사용 개수 저장
            price -= x*change
            #현재 돌고 있는 money * 그 money의 개수를 주어진 가격에서 빼기

        else:
            pay.append(0)  #몫이 0이면 그냥 0 삽입

    print(f'#{i}')
    print(*pay)
