t=int(input())
for s in range(t):
    n=int(input())
    lst = list(input().split())
    mid=(n+1)//2
    a=lst[:mid]
    b=lst[mid:]
    ans=[]
    for i in range(len(b)):
        ans.append(a[i])
        ans.append(b[i])
    if n%2!=0:
        ans.append(a[-1])
    print(f'#{s+1}',*ans)