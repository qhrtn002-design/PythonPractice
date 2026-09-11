t= int(input())
for s in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if a[i]!=b[i]:
            cnt+=1
            for j in range(i,n):
                a[j] = 1 if a[j] == 0 else 0
    print(f'#{s+1} {cnt}')