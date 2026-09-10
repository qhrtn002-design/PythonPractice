for _ in range(10):
    tc = int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]
    ans=0
    for i in range(100):
        ans = max(ans, sum(arr[i]))
    for j in range(100):
        ans2=0
        for i in range(100):
            ans2+=arr[i][j]
        ans=max(ans,ans2)
    ans3=sum(arr[i][i] for i in range(100))
    ans4=sum(arr[i][99-i] for i in range(100))
    ans=max(ans,ans3,ans4)

    print(f'#{tc} {ans}')