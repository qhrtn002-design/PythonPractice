t = int(input())

for s in range(1,t+1):
    num = int(input())
    
    arr = []
    for _ in range(num):
        lst = list(map(int,input().split()))
        arr.append(lst)

    center = num // 2

    for i in range(num):
        for j in range(num):
            abs(i -center) + abs(j - center)