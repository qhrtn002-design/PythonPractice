a = int(input())

for i in range(1,a+1):
    sum = 0
    num = list(map(int,input().split()))
    for j in num:
        sum += j
    average = sum/len(num)
    print(f'#{i} {round(average)}')