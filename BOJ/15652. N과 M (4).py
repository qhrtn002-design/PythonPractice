n,m = map(int, input().split())
ans=[]
def comb(num, idx):
    if num == m:
        print(*ans)
        return
    for i in range(idx,n+1):
        ans.append(i)
        comb(num+1,i)
        ans.pop()
comb(0,1)