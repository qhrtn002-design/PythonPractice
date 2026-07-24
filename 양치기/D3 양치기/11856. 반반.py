t = int(input())
for s in range(1,t+1):
    n = input()
    cnt = 0
    ans = 'No'
    if len(set(n)) == 2:
        ans = 'Yes'
        for i in n:
            for j in n:
                if i == j:
                    cnt += 1
            if cnt == 2:
                ans = 'Yes'
                break
    
    print(f'#{s} {ans}')