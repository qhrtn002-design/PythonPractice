import math
t = int(input())
for s in range(1,t+1):
    n , d = map(int, input().split())
    spray = 2*d+1
    ans = math.ceil(n/spray)

    print(f'#{s} {ans}')