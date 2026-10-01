t=int(input())
for s in range(t):
    n=int(input())
    lst = list(map(int, input().split()))
    ans=[]
    cnt=1
    for i in range(n-1):
        cnt = cnt +1 if lst[i]<lst[i+1] else 1
        ans.append(cnt)
    print(f'#{s+1} {max(ans)}')