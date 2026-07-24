t = int(input())
for s in range(1,t+1):
    n, k = map(int, input().split())
    lst = list(map(int,input().split()))

    ans = []
    for i in range(1,n+1):
        if i not in lst:
            ans.append(i)
        ans.sort()
    print(f'#{s} ',end='')
    print(*ans)