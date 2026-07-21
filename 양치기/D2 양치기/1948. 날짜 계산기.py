t = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for s in range(1,t+1):
    ans1, ans2 = 0, 0
    m1, d1, m2, d2 = map(int,input().split())

    for i in range(m1):
        ans1 += day[i]
    ans1 += d1
    for i in range(m2):
        ans2 += day[i]
    ans2 += d2

    print(f'#{s} {ans2-ans1+1}')