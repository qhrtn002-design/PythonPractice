t = int(input())

for s in range(1,t+1):
    num = int(input())
    
    arr = [list(map(int,input())) for _ in range(num)]

    center = num // 2
    total = 0 

    for i in range(num):
        dis = abs(center - i)
        total += sum(arr[i][dis: num-dis])

    print(f'#{s} {total}')