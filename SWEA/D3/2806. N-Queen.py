def start(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for i in range(n):
        queen[row] = i
        if check(row,i):
            start(row+1)

def check(row,col):
    for i in range(row):
        if queen[i]==col or (abs(i-row)==abs(col-queen[i])):
            return False
    return True

t=int(input()) 
for s in range(t):
    n = int(input())
    cnt = 0
    queen = [0]*n
    start(0)
    print(f'#{s+1} {cnt}')