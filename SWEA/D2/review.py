#복습용
t = int(input())
for s in range(t):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for row in arr:
        if len(set(row)) != 9:
            flag = 0

    for i in range(9):
        col = []
        for j in range(9):
            col.append(arr[j][i])
        if len(set(col)) != 9:
            flag = 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            mat = []
            for x in range(3):
                for y in range(3):
                    mat.append(arr[i+x][j+y])
            if len(set(mat)) != 9:
                flag = 0

    print(f'#{s+1} {flag}')