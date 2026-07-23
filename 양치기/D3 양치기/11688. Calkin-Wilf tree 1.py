t = int(input())

for s in range(1,t+1):
    n = input()

    start = 1,1
    for i in n:
        if i == 'L':
            node = start[0], start[0]+start[1]
        else:
            node = start[0]+start[1], start[1]
        start = node

    print(f'#{s} ', end = '')
    print(*node)