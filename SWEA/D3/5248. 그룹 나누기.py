def union(x,y):
    fa = find(x)
    fb = find(y)
    if fa != fb:
        group[fb] = fa

def find(x):
    if x != group[x]:
        x = find(group[x])
    return group[x]

t = int(input())
for tc in range(t):
    n,m = map(int, input().split())
    lst = list(map(int, input().split()))
    group = [i for i in range(n+1)]
    for i in range(0,2*m,2):
        a = lst[i]
        b = lst[i+1]
        union(a,b)

    ans = set()
    for i in range(1,n+1):
        ans.add(find(i))

    print(f'#{tc+1} {len(ans)}')