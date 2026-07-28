for s in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2):
        if lst[i] > max(lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            ans += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])

    print(f'#{s+1} {ans}')