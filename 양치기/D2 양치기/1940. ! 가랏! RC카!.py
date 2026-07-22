t = int(input())

for s in range(1,t+1):
    n = int(input())
    dis = 0
    vel = 0
    for i in range(n):
        cmd = list(map(int, input().split()))
        if len(cmd) == 2:
            if cmd[0] == 1:
                vel += cmd[1]
            else:
                vel = max(0, vel - cmd[1] )
                
        dis += vel
        
    print(f'#{s} {dis}')