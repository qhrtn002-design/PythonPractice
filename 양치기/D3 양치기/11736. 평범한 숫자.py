t = int(input())

for s in range(1,t+1):
    n = int(input())
    cnt = 0
    lst = list(map(int, input().split()))
    
    for i in range(1, n-1):
        if lst[i] != max(lst[i-1:i+2]) and lst[i] != min(lst[i-1:i+2]):
            cnt += 1
    
    print(f'#{s} {cnt}')