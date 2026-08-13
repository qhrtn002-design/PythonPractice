def comb(idx,total):
    global cnt
    if idx == n:
        if total == k:
            cnt+=1
        return
    if total+lst[idx]<=k:
        comb(idx+1,total+lst[idx])
    comb(idx+1,total)
t = int(input())
for s in range(t):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    cnt = 0
    comb(0,0)
    print(f'#{s+1} {cnt}')