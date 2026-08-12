n, m = map(int, input().split())
ans = []

#중복 순열
def dupperm(num):
    if num == m:
        print(*ans)
        return
    for i in range(1, n+1):
        ans.append(i)
        dupperm(num+1)
        ans.pop()

#중복 조합
def dupcomb(num, idx):
    if num == m:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(i)
        dupcomb(num+1, i)
        ans.pop()

#조합
def comb(num, idx):
    if num == m:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(i)
        comb(num+1, i+1)
        ans.pop()

#순열
visited = [0] * (n+1)
def perm(num):
    if num == m:
        print(*ans)
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = 1
            ans.append(i)
            perm(num+1)
            ans.pop()
            visited[i] = 0