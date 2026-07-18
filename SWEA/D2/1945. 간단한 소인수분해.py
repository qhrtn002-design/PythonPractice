t = int(input())

prime = [2,3,5,7,11] # 문제에서 지정해 준 소수 저장

for i in range(1,t+1):
    num = int(input()) #숫자 받기
    
    ans = [] #정답 리스트 생성, 케이스 마다 바뀌므로 여기에 위치
    for x in prime:
        cnt = 0 # 카운트 생성, 소수마다 리셋되므로 여기에 위치

        while num % x == 0: #숫자가 현재 소수에 나눠질 때까지 반복
            num //= x #숫자는 계속 나뉘어지고,
            cnt +=1 # 카운팅은 올라간다.
        ans.append(cnt) #최종 카운팅 정답 리스트에 삽입

    print(f'#{i}',end=' ')
    print(*ans)