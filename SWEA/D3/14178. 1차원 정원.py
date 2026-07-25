import math #import 필요
t = int(input())
for s in range(1,t+1):
    n , d = map(int, input().split())
    spray = 2*d+1 #분무기 범위 일반화
    ans = math.ceil(n/spray) #범위에 미치지 못하는 구간이 남아도 올림처리

    print(f'#{s} {ans}')