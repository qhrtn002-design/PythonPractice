def union(x,y):
    fa = findboss(x)
    fb = findboss(y)
    if fa != fb:
        group[fb] = fa

def findboss(x):
    if x != group[x]:
        group[x] = findboss(group[x])
    return group[x]

t=int(input())
for tc in range(t):
    n,m=map(int,input().split())
    group=[i for i in range(n+1)]
    ans = ''
    for _ in range(m):
        p, a, b = map(int,input().split())
        if p == 0:
            union(a,b)
        else:
            if findboss(a) == findboss(b):
                ans += '1'
            else:
                ans += '0'

    print(f'#{tc+1} {ans}')