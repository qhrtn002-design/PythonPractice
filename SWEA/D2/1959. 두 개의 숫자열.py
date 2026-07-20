t = int(input())

for s in range(1, t+1):
    n, m = map(int, input().split())

    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))

    total = 0
    for x in range(len(lst_a)):
        for y in range(len(lst_b)):
            total += lst_a[x] * lst_b[y]


    print(f'#{s} {total}')