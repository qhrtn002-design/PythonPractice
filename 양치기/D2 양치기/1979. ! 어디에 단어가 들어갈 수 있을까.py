t = int(input())

for s in range(1,t+1):
    n, k = map(int, input().split())

    arr = [(list(map(int,input().split()))) for _ in range(n)]

    total = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0
        if cnt == k:
            total += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            else:
                cnt = 0
        if cnt == k:
            total += 1

    print(f'#{s} {total}')   
