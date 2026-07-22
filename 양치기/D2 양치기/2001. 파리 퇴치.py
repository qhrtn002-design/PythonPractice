t = int(input())

for s in range(1,t+1):
    n,m = map(int,input().split())

    arr = [(list(map(int,input().split()))) for _ in range(n)]
    ans = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for x in range(m):
                for y in range(m):
                    total += arr[i+x][j+y]

            if total > ans:
                ans = total

    print(f'#{s} {ans}')