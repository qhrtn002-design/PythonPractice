t = int(input())
a=b=0
for _ in range(t):
    x, y = map(int, input().split())
    a = (x+y)//2
    b = x-a
    print(a, b)