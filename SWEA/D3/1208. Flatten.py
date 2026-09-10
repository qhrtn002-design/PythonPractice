for s in range(10):
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    for _ in range(n):
        lst[-1]-=1
        lst[0]+=1
        lst.sort()
    print(f'#{s+1} {max(lst)-min(lst)}')