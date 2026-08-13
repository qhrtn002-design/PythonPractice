def dfs(row):
    global cnt
    if row == n:
        cnt+=1
        return
    for i in range(n):
        if dfs(i) == 0:
            continue
    row.append(1)
    dfs(row+1)
    row.pop()

t = int(input())
for s in range(t):
    n = int(input())
    cnt = 0
    dfs(0)
    print(f'{s+1}')