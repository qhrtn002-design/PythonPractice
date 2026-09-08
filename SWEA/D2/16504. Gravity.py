t=int(input())
for s in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    ans = 0
    for i in range(n):
        cnt=0
        for j in range(i+1,n):
            if lst[i]>lst[j]:
                cnt+=1
        ans = max(cnt,ans)
    print(f'#{s+1} {ans}')