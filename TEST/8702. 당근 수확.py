t=int(input())
for s in range(t):
    n = int(input())
    lst=list(map(int,input().split()))
    total=sum(lst)//2
    dif=[]
    for i in range(n):
        a=lst[:i]
        b=lst[i:n]
        dif.append(abs(sum(a)-sum(b)))
    print(f'#{s+1} {dif.index(min(dif))} {min(dif)}')