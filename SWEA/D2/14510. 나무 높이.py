t = int(input())

for s in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    maxh = max(lst)

    one = 0
    two = 0

    for i in lst:
        gap = maxh - i

        two += gap //2
        one += gap %2

    day = 0

    while two > one + 1:
        two -= 1
        one += 2

    if one > two:
        ans = one * 2 -1
    elif one == two:
        ans = one * 2
    else:
        ans = two * 2
        
    print(f'#{s} {ans}')
            