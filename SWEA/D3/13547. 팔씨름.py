t = int(input())

for s in range(1,t+1):
    n = input()
    cnt = 0
    for i in n:
        if i == 'x': #X 카운팅
            cnt += 1
    ans = 'NO' if cnt >= 8 else 'YES' 
    #X 개수가 절반넘으면 이길가능성없음
    print(f'#{s} {ans}')