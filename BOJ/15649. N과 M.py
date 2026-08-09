
n, m = map(int, input().split())
ans = []
visited = [0]*(n+1)
def dfs(num):
    if num == m :
        print(*ans)
        return
    for i in range(1,n+1):
        if not visited[i]:

            visited[i] = 1
            ans.append(i)
            dfs(num+1)
            ans.pop()
            visited[i] = 0
dfs(0)