num = int(input())

for i in range(1, num+1):
    a, b = map(int, input().split())
    if a//10 >= 1 or b//10 >=1:
        ans = -1
    else:
        ans = a*b
    print(f'#{i} {ans}')