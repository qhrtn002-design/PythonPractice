t = int(input())
for s in range(1, t+1):
    n = int(input())
    cnt = 0 
    for x in range(-n,n+1): #원 안의 범위를 구하므로 음수까지 생각
        for y in range(-n,n+1):
            if ((x**2)+(y**2))<=n**2: 
                cnt +=1 #원점 기준으로 면적안에드는 x,y 개수 카운팅

    print(f'#{s} {cnt}')