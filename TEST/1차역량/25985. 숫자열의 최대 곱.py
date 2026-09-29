t= int(input())
for s in range(t):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    ans=float('-inf')
    if len(a)>len(b):
        pad = [0]*(m-1)+a+[0]*(m-1)
        for k in range(len(a)+len(b)-1):
            mul=0
            for i in range(m):
                mul += pad[i+k]*b[i]
            ans=max(ans,mul)
    else:
        pad = [0]*(n-1)+b+[0]*(n-1)
        for k in range(len(a)+len(b)-1):
            mul=0
            for i in range(n):
                mul+=pad[i+k]*a[i]
            ans=max(ans,mul)
    print(f'#{s+1} {ans}')