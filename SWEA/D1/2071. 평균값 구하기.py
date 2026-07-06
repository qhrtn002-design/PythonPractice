a = int(input())

for i in range(a):
    num = 0
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        num += arr[j]
    avg = num / len(arr)
    print("#%d %d" % (i+1, round(avg,1)))