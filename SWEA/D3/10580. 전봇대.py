t=int(input())
for s in range(t):
    n=int(input())
    lst=[]
    for _ in range(n):
        a,b=map(int, input().split())
        lst.append([a,b])
    lst.sort()
    cnt=0
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i][1]>lst[j][1]:
                cnt+=1
    print(f'#{s+1} {cnt}')