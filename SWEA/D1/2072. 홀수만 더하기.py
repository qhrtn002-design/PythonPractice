a = int(input())

for i in range(a):
    num = 0
    arr = list(map(int, input().split()))
    for j in range(len(arr)):

        if arr[j] % 2 == 1:
            num += arr[j]
    print("#%d %d" % (i+1, num))