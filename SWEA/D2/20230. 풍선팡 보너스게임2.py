t=int(input())
for s in range(t):
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(n):
            total_row=sum(arr[i])
            total_col = 0

            for k in range(n):
                total_col += arr[k][j]

            total = total_col + total_row - arr[i][j]
            ans=max(ans,total)

    print(f'#{s+1} {ans}')