t=int(input())
for s in range(t):
    n=int(input())
    arr=[list(map(int,input()))for _ in range(n)]
    ans = 0 
    center = n//2
    for i in range(n):
        ans+=sum(arr[i][abs(center-i):n-abs(center-i)])
    print(f'#{s+1} {ans}')