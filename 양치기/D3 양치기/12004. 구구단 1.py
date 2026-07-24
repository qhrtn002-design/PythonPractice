t = int(input())
for s in range(1,t+1):
    n = int(input())
    ans = 'No'
    for i in range(1,10):
        for j in range(1,10):
            if n == i*j:
                ans = 'Yes'
        
    print(f'#{s} {ans}')