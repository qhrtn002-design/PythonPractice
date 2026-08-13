def comb(idx, score, cal):
    if cal > l:
        print(score)
        return
    for i in range(idx, n):
        ans.append()
        comb(idx+1, score+h1, cal+h2)
        ans.pop()

t = int(input())
for s in range(t):
    n, l = map(int, input().split())
    for _ in range(n):
        h1, h2 = map(int, input().split())
        ans = []
        comb(0,0,0)

