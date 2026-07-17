t = int(input())

for i in range(1,t+1):
    num = int(input()) # 테스트 케이스에서 숫자 받기

    ans = 0 #초기 정답 지정
    for j in range(1,num+1): #1부터 주어진 숫자만큼 반복하는데,
        if j % 2 == 1: #숫자가 홀수이면 더하고,
            ans += j
        else: # 짝수이면 뺀다
            ans -= j

    print(f'#{i} {ans}') #최종 답 출력