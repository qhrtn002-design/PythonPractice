t = int(input())
for s in range(t):
    n = int(input())
    total = 0
    center = n//2
    arr = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        distance = abs(center-i)
        total += sum(arr[i][distance:n-distance])
    print(f'#{s+1} {total}')