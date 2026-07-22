t = int(input())

for _ in range(1,t+1):
    p, q, r, s, w = map(int, input().split())

    A = p * w
    if w <= r:
        B = q
    else:
        B = q + (w-r)*s

    if A<B:
        ans = A
    else:
        ans = B

    print(f'#{_} {ans}')