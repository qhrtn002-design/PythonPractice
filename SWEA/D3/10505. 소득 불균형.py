t = int(input())

for s in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    avg = int(sum(lst)/len(lst)) #평균구하기
    for i in lst:
        if i <= avg: #리스트 값이 평균 미만이면 개수 세기
            cnt += 1
    print(f'#{s} {cnt}')