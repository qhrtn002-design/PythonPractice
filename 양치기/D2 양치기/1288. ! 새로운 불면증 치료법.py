t = int(input())

for s in range(1,t+1):
    n = int(input())
    k=1
    answer = set() #집합 지정

    while len(answer) != 10:
        num = n * k
        ans = str(num) #숫자 문자열로 바꾸고

        answer.update(ans) #집합에 넣기. update 사용
        k+=1 #넣은 후 배수 증가

    print(f'#{s} {num}')