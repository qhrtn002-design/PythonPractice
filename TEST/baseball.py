t=int(input())
for s in range(t):
    ans=1
    n,k=map(int, input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    for i in range(n-1):
        temp=1
        for j in range(i+1,n):
            if lst[j]-lst[i]<=k:
                temp+=1
            else:
                break
        ans=max(ans,temp)

    print(f'#{s+1} {ans}')