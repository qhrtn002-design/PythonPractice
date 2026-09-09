num=[1,2,3,4]
m=2
pick=[]
visited=[0]*len(num)
def perm(cnt):
    if cnt == m:
        print(*pick)
        return
    for i in range(len(num)):
        if visited[i]:
            continue
        pick.append(num[i])
        visited[i] = 1
        perm(cnt+1)
        pick.pop()
        visited[i] = 0
# perm(0)

def comb(cnt,idx):
    if cnt==m:
        print(*pick)
        return
    for i in range(idx,len(num)):
        pick.append(num[i])
        comb(cnt+1,i+1)
        pick.pop()

comb(0,0)
