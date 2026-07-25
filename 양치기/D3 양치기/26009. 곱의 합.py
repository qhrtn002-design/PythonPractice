t = int(input())
for s in range(1,t+1):
    a,b,c = map(int, input().split())

    num1 = a*(a+1)//2
    num2 = b*(b+1)//2
    num3 = c*(c+1)//2
    total = num1*num2*num3
    x = 998244353
    print(total%x)
