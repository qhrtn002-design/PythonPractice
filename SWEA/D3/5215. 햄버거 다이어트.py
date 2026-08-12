def comb():
    if num == m:
        return
    for i in range(idx, n):
        ans.append(i)
        comb(num+1, i+1)
        ans.pop()

t = int(input())
for s in range(t):
    n, l = map(int, input().split())
    for _ in range(n):
        h1, h2 = map(int, input().split())
        ans = []
        comb()

