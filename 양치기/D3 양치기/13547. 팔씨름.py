t = int(input())

for s in range(1,t+1):
    n = input()
    cnt = 0
    for i in n:
        if i == 'x':
            cnt += 1
    ans = 'NO' if cnt >= 8 else 'YES'
    print(f'#{s} {ans}')