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
    n = int(input())
    ans=0
    x=list(map(int, input().split()))
    y=list(map(int, input().split()))
    e = float(input())
    edge = []
    group = [i for i in range(n+1)]
    for i in range(n):
        for j in range(i+1,n):
            dis = (x[i]-x[j])**2 + (y[i]-y[j])**2
            edge.append((dis,i,j))
    edge.sort()

    for dis,i,j in edge:
        if find(i)!= find(j):
            union(i,j)
            ans += dis
    ans = round(ans*e)
    print(f'#{tc+1} {ans}')