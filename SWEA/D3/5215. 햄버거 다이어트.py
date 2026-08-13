def comb(idx, score, cal):
    global max_sco
    if idx == n:
        if max_sco<score:
            max_sco=score
        return
    if cal + burger[idx][1] <= l:
        comb(idx+1, score+burger[idx][0], cal+burger[idx][1])
    comb(idx+1,score,cal)

t = int(input())
for s in range(t):
    burger = [] 
    max_sco = 0
    n, l = map(int, input().split())
    for _ in range(n):
        h1, h2 = map(int, input().split())
        burger.append((h1,h2))
    comb(0,0,0)
    print(f'#{s+1} {max_sco}')