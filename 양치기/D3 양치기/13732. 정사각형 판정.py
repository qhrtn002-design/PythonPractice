t = int(input())
for s in range(1,t+1):
    n = int(input())
    arr = [list(input())for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == '#':
                c1, c2 = i, j

    for x in range(c1, n):
        cnt = 0
        for y in range(c2, n):
            if arr[c1][c2] == '#':
                cnt += 1
        if cnt == (n-j) * (n-i):
            ans = 'yes'
        else:
            ans = 'no'

    print(f'#{s} {ans}')