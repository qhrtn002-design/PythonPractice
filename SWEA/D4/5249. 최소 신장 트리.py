def union(a,b):
    fa = find(a)
    fb = find(b)
    if fa!=fb:
        group[fa] = fb

def find(x):
    if x != group[x]:
        group[x] = find(group[x])
    return group[x]

t=int(input())
for tc in range(t):
    v,e = map(int,input().split())
    group = [i for i in range(v+1)]
    edge=[]
    ans = 0
    for _ in range(e):
        a,b,c = map(int,input().split())
        edge.append((c,a,b))
    edge.sort()

    for c,a,b in edge:
        if find(a) != find(b):
            union(a,b)
            ans +=c

    print(f'#{tc+1} {ans}')