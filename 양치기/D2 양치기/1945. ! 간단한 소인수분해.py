t = int(input())
prime = [2,3,5,7,11]

for s in range(1,t+1):
    num = int(input())
    ans = []
    
    for i in prime: #소수 리스트 하나씩 꺼내기
        cnt = 0 #카운트 생성 소수당 초기화 위치

        if num % i == 0: #소수가 나뉘어지면
            while num % i == 0: #안나눠질때까지 반복
                # 조건이 거짓이 될때까지 반복
                num //= i
                cnt += 1
        ans.append(cnt)

    print(f'#{s}',end=' ')
    print(*ans)