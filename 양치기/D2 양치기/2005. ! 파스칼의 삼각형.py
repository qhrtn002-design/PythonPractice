t = int(input())

for s in range(1,t+1):
    n = int(input())
    print(f'#{s}')
    prev = []
    for i in range(n):
        arr = []
        for j in range(i+1):
            if j == 0 or j == i:
                arr.append(1)
            else:
                arr.append(prev[j]+prev[j-1])

        prev = arr
        print(*arr)