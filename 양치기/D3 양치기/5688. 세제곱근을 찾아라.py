import math
t = int(input())
for s in range(1,t+1):
    n = int(input())
    x = math.ceil(n**(1/3))
    ans = x if x**3==n else -1
    print(f'#{s} {ans}')