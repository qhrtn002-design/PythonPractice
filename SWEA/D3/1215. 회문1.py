for s in range(10):
    n=int(input())
    arr=list(input() for _ in range(8))
    ans=0
    for i in range(8):
        for j in range(8-n+1):
            text = arr[i][j:j+n]
            if text==text[::-1]:
                ans+=1
    for j in range(8):
        for i in range(8-n+1):
            text = ''.join(arr[i+k][j] for k in range(n))
            if text==text[::-1]:
                ans+=1
    print(f'#{s+1} {ans}')