t = int(input())
MOD = 1000000007
for s in range(t):
    n = int(input())
    spd = []
    for _ in range(n):
        a, b = map(int, input().split())
        spd.append([a, b])
    spd.sort(key=lambda x: x[1] / (x[0] - 1) if x[0] != 1 else float('inf'))
    v = 1
    for a, b in spd:
        v = (a * v + b) % MOD
    print(f'#{s+1} {v}')