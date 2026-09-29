t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    idx=0
    ans='NO'
    for i in range(n):
        if a[i] == b[idx]:
            idx+=1
        if idx == m:
            ans='YES'
            break
    print(f'#{s+1} {ans}')