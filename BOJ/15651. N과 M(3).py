n, m = map(int,input().split())
ans = []
def perm(num):
    if num == m:
        print(*ans)
        return
    for i in range(1, n+1):
        ans.append(i)
        perm(num+1)
        ans.pop()
perm(0)