t = int(input())

for s in range(1,t+1):
    flag = 1

    arr = [(list(map(int,input().split()))) for _ in range(9)]

    for x in arr:
        if len(set(x)) != 9:
            flag = 0

    for y in range(9):
        col = []
        for x in range(9):
            col.append(arr[x][y])
        if len(set(col)) != 9:
            flag = 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            test=[]
            for a in range(3):
                for b in range(3):
                    test.append(arr[a+i][b+j])
            if len(set(test)) != 9:
                flag = 0

    print(f'#{s} {flag}')

    