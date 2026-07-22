t = int(input())

def rotate(arr):
    newarr = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            newarr[j][n-i-1] = arr[i][j]

    return newarr

for s in range(1,t+1):
    n = int(input())

    arr = [(list(map(int, input().split()))) for _ in range(n)]

    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    print(f'#{s}')
    for ct in range(n):
        print(''.join(map(str,arr90[ct])),
              ''.join(map(str,arr180[ct])),
              ''.join(map(str,arr270[ct])))
        