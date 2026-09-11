t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    if len(a)>len(b):
        for k in range(abs(n-m)+1):
            total=0
            for i in range(m):
                total+=a[i+k]*b[i]
            ans=max(ans,total)
    else:
        for k in range(abs(n-m)+1):
            total=0
            for i in range(n):
                total+=a[i]*b[i+k]
            ans=max(ans,total)
    print(f'#{s+1} {ans}')