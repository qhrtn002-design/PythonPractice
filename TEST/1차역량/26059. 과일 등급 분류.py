t=int(input())
for s in range(t):
    n, l, h = map(int, input().split())
    w=list(map(int, input().split()))
    w.sort()
    lst=[]
    ans=-1
    for i in range(n-1):
        if w[i]!=w[i+1]:
            lst.append(i+1)
    for k in range(len(lst)):
        for j in range(k+1, len(lst)):
            a=lst[k]
            b=lst[j]

            cnt1=a
            cnt2=b-a
            cnt3=n-b

            if l <= cnt1 <= h and l <= cnt2 <= h and l <= cnt3 <= h:
                dif = max(cnt1,cnt2,cnt3) - min(cnt1,cnt2,cnt3)
                ans = dif if ans == -1 else min(ans,dif)
    print(f'#{s+1} {ans}')