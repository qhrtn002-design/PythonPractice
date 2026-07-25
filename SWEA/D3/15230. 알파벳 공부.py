t = int(input())

for s in range(1,t+1):
    n = input()
    cnt = 1 #초기값 1 = 모두 만족해야한다
    if n[0] != 'a': #문자열 시작이 a가 아니면 바로 커트
        cnt = 0
    else: # a로 시작해도,
        for i in range(1,len(n)): 
            #문자와 다음 문자의 차이가 아스키코드로 1이 나야 연속된 문자
            if ord(n[i-1])-ord(n[i]) == -1:
                cnt += 1
            else:
                break
                
    print(f'#{s} {cnt}')