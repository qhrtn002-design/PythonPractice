t = int(input())
for s in range(1,t+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    point = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                point.append((i,j))
    r1 = min(x[0] for x in point)
    r2 = max(x[0] for x in point)
    c1 = min(x[1] for x in point)
    c2 = max(x[1] for x in point)
    ans = 'yes'
    rowsize, colsize = r2-r1+1, c2-c1+1

    if rowsize != colsize:
        ans = 'no'
    else:
        for i in range(r1,r2+1):
            for j in range(c1, c2+1):
                if arr[i][j] != '#':
                    ans = 'no'
    print(f'#{s} {ans}')