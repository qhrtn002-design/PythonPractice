t=int(input())
for s in range(t):
    n=int(input())
    alst=list(map(int,input().split()))
    blst=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if alst[i] != blst[i]:
            cnt+=1
            for j in range(i,n):
                if alst[j] == 0:
                    alst[j] = 1
                else:
                    alst[j] = 0

    print(f'#{s+1} {cnt}')