t = int(input())

for s in range(1,t+1):
    n = input()
    cnt = 1
    if n[0] != 'a':
        cnt = 0
    else:
        for i in range(1,len(n)):
            if ord(n[i-1])-ord(n[i]) == -1:
                cnt += 1
            else:
                break
                
    print(f'#{s} {cnt}')