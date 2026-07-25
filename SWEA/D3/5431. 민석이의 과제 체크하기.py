t = int(input())
for s in range(1,t+1):
    n, k = map(int, input().split())
    lst = list(map(int,input().split()))

    ans = []
    for i in range(1,n+1): #1부터 n만큼 반복하는데
        if i not in lst: #리스트에 없으면 넣고, 이후 정렬
            ans.append(i)
        ans.sort()
    print(f'#{s} ',end='')
    print(*ans)