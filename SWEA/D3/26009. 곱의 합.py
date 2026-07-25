t = int(input())
for s in range(1,t+1):
    a,b,c = map(int, input().split())

    num1 = a*(a+1)//2 #등차수열 합공식. 해당 시그마 하나의 전체 값
    num2 = b*(b+1)//2
    num3 = c*(c+1)//2
    total = num1*num2*num3 #시그마끼린 곱하기 가능
    x = 998244353
    print(total%x)
