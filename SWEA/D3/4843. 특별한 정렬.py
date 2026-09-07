t=int(input())
for s in range(t):
    n=int(input())
    lst=list(map(int, input().split()))
    ans=[]
    lst.sort()
    for i in range(n):
        ans.append(lst[-i-1])
        ans.append(lst[i])
        if len(ans)==10:
            break
    print(f'#{s+1}', *ans)