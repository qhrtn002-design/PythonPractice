t = int(input())

for s in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    avg = int(sum(lst)/len(lst))
    for i in lst:
        if i <= avg:
            cnt += 1
    print(f'#{s} {cnt}')