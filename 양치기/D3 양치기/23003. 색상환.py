t = int(input())
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for s in range(1,t+1):
    a, b = input().split()
    if a in color:
        n1 = color.index(a)
    if b in color:
        n2 = color.index(b)

    dis = abs(n1-n2)
    if dis == 0:
        ans = 'E'
    elif dis == 1:
        ans = 'A'
    elif dis == 2:
        ans = 'X'
    elif dis == 3:
        ans = 'C'
    elif dis == 4:
        ans = 'X'
    elif dis == 5:
        ans = 'A'

    print(ans)